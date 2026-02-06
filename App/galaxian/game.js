import { CONSTANTS } from './js/constants.js';
import { InputHandler } from './js/input.js';
import { Starfield } from './js/starfield.js';
import { SoundManager } from './js/audio.js';
import { Player, Enemy, Bullet, Particle } from './js/entities.js';

class Game {
    constructor() {
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');

        // Set internal resolution
        this.canvas.width = CONSTANTS.SCREEN_WIDTH;
        this.canvas.height = CONSTANTS.SCREEN_HEIGHT;

        this.input = new InputHandler(this.canvas);
        this.starfield = new Starfield(this.canvas);
        this.audio = new SoundManager();

        this.player = null;
        this.enemies = [];
        this.bullets = [];
        this.particles = [];

        this.state = CONSTANTS.STATE_MENU;
        this.lastTime = 0;
        this.time = 0;

        this.score = 0;
        this.highScore = parseInt(localStorage.getItem('galaxian_highscore')) || 0;
        this.level = 1;
        this.lives = 3;

        this.updateHUD(); // Show high score initially

        this.resize();
        window.addEventListener('resize', () => this.resize());

        // Input hook for starting game
        this.input.onTap = () => this.handleGlobalInput();

        this.loop = this.loop.bind(this);
        requestAnimationFrame(this.loop);
    }

    resize() {
        const container = document.getElementById('game-container');
        const aspect = CONSTANTS.SCREEN_WIDTH / CONSTANTS.SCREEN_HEIGHT;
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;

        let w, h;

        if (containerWidth / containerHeight < aspect) {
            w = containerWidth;
            h = w / aspect;
        } else {
            h = containerHeight;
            w = h * aspect;
        }

        // CSS scaling for the canvas to keep Aspect Ratio correct
        // The internal resolution remains 600x800, CSS scales it visibly
        // But to ensure Input mapping is correct, we checked that in InputHandler
        // Actually for crisp pixel art, it might be better to let canvas fill container
        // and scale ctx, but let's stick to fixed internal resolution + CSS scale for simplicity/retro feel.
        // Wait, "Perfect adaptation to all screen sizes" and "Object size optimized for mobile"
        // Let's trust the CSS object-fit or simple max-width containment we set up in style.css.
        // The canvas.width/height is the logical resolution.

        // Update input scale if needed (since we rely on internal resolution)
        // ClientRect in InputHandler handles the mapping from Screen -> Canvas logic.
    }

    handleGlobalInput() {
        if (this.state === CONSTANTS.STATE_MENU) {
            this.audio.resume();
            this.startGame();
        } else if (this.state === CONSTANTS.STATE_GAMEOVER) {
            this.resetGame();
        }
    }

    startGame() {
        this.state = CONSTANTS.STATE_PLAYING;
        document.getElementById('start-screen').classList.remove('active');
        document.getElementById('start-screen').classList.add('hidden');
        document.getElementById('game-over-screen').classList.add('hidden');

        this.audio.startMusic();

        this.score = 0;
        this.lives = 3;
        this.level = 1;
        this.resetLevel();
    }

    resetLevel() {
        this.player = new Player(this);
        this.enemies = [];
        this.bullets = [];
        this.particles = [];
        this.powerups = [];
        this.spawnEnemies();
        this.updateHUD();
    }

    spawnEnemies() {
        const isMobile = window.innerWidth <= 480;
        const rows = CONSTANTS.ENEMY_ROWS;
        const cols = isMobile ? CONSTANTS.ENEMY_COLS_MOBILE : CONSTANTS.ENEMY_COLS;
        const startX = (CONSTANTS.SCREEN_WIDTH - (cols * 40)) / 2;
        const startY = 50;

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                // Type based on row
                let type = 0;
                if (r === 0) type = 2; // Red top
                else if (r === 1) type = 1; // Purple mid

                const enemy = new Enemy(this, startX + c * 40, startY + r * 35, type);
                this.enemies.push(enemy);
            }
        }
    }

    resetGame() {
        this.state = CONSTANTS.STATE_MENU;
        document.getElementById('game-over-screen').classList.remove('active');
        document.getElementById('game-over-screen').classList.add('hidden');
        document.getElementById('start-screen').classList.remove('hidden');
        document.getElementById('start-screen').classList.add('active');
    }

    gameOver() {
        this.state = CONSTANTS.STATE_GAMEOVER;
        this.audio.stopMusic();

        if (this.score > this.highScore) {
            this.highScore = this.score;
            localStorage.setItem('galaxian_highscore', this.highScore);
        }

        document.getElementById('final-score').innerText = this.score;
        document.getElementById('game-over-screen').classList.remove('hidden');
        document.getElementById('game-over-screen').classList.add('active');
        this.updateHUD();
    }

    updateHUD() {
        document.getElementById('score').innerText = this.score;
        document.getElementById('high-score').innerText = this.highScore;
        document.getElementById('lives').innerText = this.lives;
        document.getElementById('level').innerText = this.level;

        // Shield visual in HUD
        const s = this.player ? this.player.shield : 0;
        document.getElementById('shield-bar').innerText = '█'.repeat(s);
    }

    update(dt) {
        this.time += dt;
        this.starfield.update();

        if (this.state === CONSTANTS.STATE_PLAYING) {
            if (this.player) this.player.update();

            this.enemies.forEach(e => e.update());
            this.bullets.forEach(b => b.update());
            this.particles.forEach(p => p.update());
            this.powerups.forEach(p => p.update());

            // Clean up
            this.bullets = this.bullets.filter(b => !b.markedForDeletion);
            this.particles = this.particles.filter(p => !p.markedForDeletion);
            this.powerups = this.powerups.filter(p => !p.markedForDeletion);

            // Collisions (Simple AABB)
            this.checkCollisions();
        }
    }

    checkCollisions() {
        if (!this.player) return;

        // Bullet collisions
        this.bullets.forEach(b => {
            // Player Bullet vs Enemy
            if (b.isPlayer) {
                this.enemies.forEach(e => {
                    if (!e.markedForDeletion && this.checkAABB(b, e)) {
                        e.markedForDeletion = true;
                        b.markedForDeletion = true;

                        this.spawnExplosion(e.x + e.width / 2, e.y + e.height / 2, CONSTANTS.COLOR_NEON_PINK);
                        this.score += CONSTANTS.SCORE_KILL;
                        this.audio.playEnemyHit();
                        this.updateHUD();

                        // Drop powerup chance
                        if (Math.random() < 0.1) {
                            this.spawnPowerUp(e.x, e.y);
                        }
                    }
                });
            } else {
                // Enemy Bullet vs Player
                if (this.checkAABB(b, this.player)) {
                    b.markedForDeletion = true;
                    this.damagePlayer();
                }
            }
        });

        // Enemy Body vs Player Body
        this.enemies.forEach(e => {
            if (!e.markedForDeletion && this.checkAABB(e, this.player)) {
                e.markedForDeletion = true;
                this.damagePlayer();
            }
        });

        // PowerUp vs Player
        this.powerups.forEach(p => {
            if (!p.markedForDeletion && this.checkAABB(p, this.player)) {
                p.markedForDeletion = true;
                this.collectPowerUp(p);
            }
        });

        this.enemies = this.enemies.filter(e => !e.markedForDeletion);

        // Next Level check
        if (this.enemies.length === 0) {
            this.level++;
            this.resetLevel();
        }
    }

    checkAABB(a, b) {
        return (a.x < b.x + b.width &&
            a.x + a.width > b.x &&
            a.y < b.y + b.height &&
            a.y + a.height > b.y);
    }

    damagePlayer() {
        if (this.player.shield > 0) {
            this.player.shield--;
            this.audio.playExplosion(); // Shield hit sound
            this.updateHUD();
        } else {
            this.lives--;
            this.audio.playExplosion();
            this.spawnExplosion(this.player.x + this.player.width / 2, this.player.y + this.player.height / 2, CONSTANTS.COLOR_NEON_BLUE);
            this.updateHUD();

            if (this.lives <= 0) {
                this.gameOver();
            } else {
                // Respawn effect?
                // For now, simple flash reset
                this.player.x = CONSTANTS.SCREEN_WIDTH / 2;
            }
        }
    }

    spawnPowerUp(x, y) {
        const r = Math.random();
        let type = 'HEART';
        if (r < 0.25) type = 'SHIELD';
        else if (r < 0.5) type = 'TRIPLE';
        else if (r < 0.75) type = 'WINGMEN'; // New type

        this.powerups.push(new PowerUp(x, y, type));
    }

    collectPowerUp(p) {
        this.audio.playPowerUp();
        if (p.type === 'HEART') {
            this.lives++;
        } else if (p.type === 'SHIELD') {
            this.player.shield += 2;
        } else if (p.type === 'TRIPLE') {
            this.player.weaponLevel = 2;
        } else if (p.type === 'WINGMEN') {
            this.player.hasWingmen = true;
        }
        this.updateHUD();
    }

    spawnExplosion(x, y, color) {
        for (let i = 0; i < 10; i++) {
            this.particles.push(new Particle(
                x, y,
                (Math.random() - 0.5) * 5,
                (Math.random() - 0.5) * 5,
                color,
                20 + Math.random() * 20
            ));
        }
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.starfield.draw();

        if (this.state === CONSTANTS.STATE_PLAYING) {
            if (this.player) this.player.draw(this.ctx);
            this.powerups.forEach(p => p.draw(this.ctx));
            this.enemies.forEach(e => e.draw(this.ctx));
            this.bullets.forEach(b => b.draw(this.ctx));
            this.particles.forEach(p => p.draw(this.ctx));
        }
    }

    loop(timestamp) {
        const dt = timestamp - this.lastTime;
        this.lastTime = timestamp;

        this.update(dt);
        this.draw();

        requestAnimationFrame(this.loop);
    }
}

// Start the game
window.game = new Game();
