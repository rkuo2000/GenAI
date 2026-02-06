import { CONSTANTS } from './constants.js';

// --- Sprite Helper ---
// Creates an offscreen canvas for a pixel art sprite
function createPixelSprite(matrix, color, pixelSize = 2) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    const canvas = document.createElement('canvas');
    canvas.width = cols * pixelSize;
    canvas.height = rows * pixelSize;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = color;
    ctx.shadowBlur = 4;
    ctx.shadowColor = color;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (matrix[r][c] === 1) {
                ctx.fillRect(c * pixelSize, r * pixelSize, pixelSize, pixelSize);
            }
        }
    }
    return canvas;
}

// 8-bit Sprite Definitions (0/1 matrices)
const SPRITES = {
    PLAYER: [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1]
    ],
    ENEMY_BLUE: [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0]
    ],
    ENEMY_PURPLE: [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1]
    ],
    ENEMY_RED: [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0]
    ]
};

// --- Entities ---

export class Player {
    constructor(game) {
        this.game = game;
        this.width = CONSTANTS.PLAYER_WIDTH;
        this.height = CONSTANTS.PLAYER_HEIGHT;
        this.x = CONSTANTS.SCREEN_WIDTH / 2 - this.width / 2;
        this.y = CONSTANTS.SCREEN_HEIGHT - 60;
        this.speed = CONSTANTS.PLAYER_SPEED;

        this.shootTimer = 0;
        this.weaponLevel = 1; // 1: Single, 2: Triple
        this.shield = 0;
        this.hasWingmen = false;

        // Generate sprite
        this.sprite = createPixelSprite(SPRITES.PLAYER, CONSTANTS.COLOR_NEON_BLUE, 4);
    }

    update() {
        // Movement
        if (this.game.input.keys.left) {
            this.x -= this.speed;
        }
        if (this.game.input.keys.right) {
            this.x += this.speed;
        }

        // Touch/Mouse Follow logic
        if (this.game.input.touchX !== null) {
            const dx = this.game.input.touchX - (this.x + this.width / 2);
            if (Math.abs(dx) > this.speed) {
                this.x += Math.sign(dx) * this.speed;
            } else {
                this.x = this.game.input.touchX - this.width / 2;
            }
        }

        // Clamp
        this.x = Math.max(0, Math.min(CONSTANTS.SCREEN_WIDTH - this.width, this.x));

        // Shooting
        if (this.game.input.keys.shoot) {
            this.shoot();
        }
        if (this.shootTimer > 0) this.shootTimer--;

        // Shield decay logic or visual update could go here
    }

    shoot() {
        if (this.shootTimer <= 0) {
            // Spawn bullet
            const spawnBullet = (xOffset, angle = 0) => {
                const b = new Bullet(
                    this.x + this.width / 2 + xOffset,
                    this.y,
                    -10,
                    CONSTANTS.COLOR_NEON_BLUE,
                    true
                );
                if (angle !== 0) {
                    b.vx = Math.sin(angle) * 5;
                    b.vy = -Math.cos(angle) * 10;
                }
                this.game.bullets.push(b);
            };

            spawnBullet(0);

            if (this.weaponLevel >= 2) {
                spawnBullet(-10, -0.1);
                spawnBullet(10, 0.1);
            }

            if (this.hasWingmen) {
                spawnBullet(-20);
                spawnBullet(20);
            }

            this.game.audio.playShoot();
            this.shootTimer = CONSTANTS.PLAYER_SHOOT_DELAY;
        }
    }

    draw(ctx) {
        ctx.drawImage(this.sprite, this.x, this.y, this.width, this.height);

        // Wingmen Visual
        if (this.hasWingmen) {
            ctx.drawImage(this.sprite, this.x - 25, this.y + 10, this.width / 1.5, this.height / 1.5);
            ctx.drawImage(this.sprite, this.x + 35, this.y + 10, this.width / 1.5, this.height / 1.5);
        }

        // Shield Visual
        if (this.shield > 0) {
            ctx.save();
            ctx.globalAlpha = 0.5;
            ctx.strokeStyle = CONSTANTS.COLOR_NEON_BLUE;
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(this.x + this.width / 2, this.y + this.height / 2, this.width, 0, Math.PI * 2);
            ctx.stroke();
            ctx.restore();
        }

        // Engine effect
        if (Math.random() > 0.5) {
            ctx.fillStyle = CONSTANTS.COLOR_NEON_BLUE;
            ctx.fillRect(this.x + this.width / 2 - 2, this.y + this.height, 4, 10 + Math.random() * 5);
        }
    }
}

export class Bullet {
    constructor(x, y, vy, color, isPlayer) {
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = vy;
        this.color = color;
        this.width = 4;
        this.height = 12;
        this.isPlayer = isPlayer;
        this.markedForDeletion = false;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        if (this.y < -20 || this.y > CONSTANTS.SCREEN_HEIGHT + 20) {
            this.markedForDeletion = true;
        }

        // Trail particles
        // (Optional: add spawn particle call here)

    }

    draw(ctx) {
        ctx.fillStyle = this.color;
        ctx.shadowColor = this.color;
        ctx.shadowBlur = 5;
        ctx.fillRect(this.x - this.width / 2, this.y, this.width, this.height);
        ctx.shadowBlur = 0;
    }
}

export class Enemy {
    constructor(game, x, y, type) {
        this.game = game;
        this.homeX = x;
        this.homeY = y;
        this.x = x;
        this.y = y;
        this.width = CONSTANTS.ENEMY_WIDTH;
        this.height = CONSTANTS.ENEMY_HEIGHT;
        this.type = type;

        let spriteData = SPRITES.ENEMY_BLUE;
        let color = CONSTANTS.COLOR_NEON_BLUE;

        if (type === 1) {
            spriteData = SPRITES.ENEMY_PURPLE;
            color = CONSTANTS.COLOR_NEON_PINK;
        } else if (type === 2) {
            spriteData = SPRITES.ENEMY_RED;
            color = CONSTANTS.COLOR_NEON_RED;
        }

        this.sprite = createPixelSprite(spriteData, color, 3);

        this.state = 'FORMATION'; // FORMATION, DIVING, RETURNING
        this.vx = 0;
        this.vy = 0;
        this.angle = 0;
        this.markedForDeletion = false;

        // Randomly dive
        this.diveTimer = Math.random() * 500 + 100;
    }

    update() {
        if (this.state === 'FORMATION') {
            // Hover in formation
            this.x = this.homeX + Math.sin(this.game.time * 0.002 + this.y * 0.05) * 10;
            this.y = this.homeY + Math.sin(this.game.time * 0.003) * 5;

            this.diveTimer--;
            if (this.diveTimer <= 0 && Math.random() < 0.005 * (1 + this.game.level * 0.5)) {
                this.startDive();
            }
        } else if (this.state === 'DIVING') {
            this.x += this.vx;
            this.y += this.vy;

            // Auto-center homing
            if (this.game.player) {
                const dx = (this.game.player.x + this.game.player.width / 2) - (this.x + this.width / 2);
                this.vx += Math.sign(dx) * 0.05 * (1 + this.game.level * 0.1);
            }

            // Wraparound
            if (this.y > CONSTANTS.SCREEN_HEIGHT) {
                this.y = -50;
                this.state = 'RETURNING';
                // Calculate vector to home
                const dx = this.homeX - this.x;
                const dy = this.homeY - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                this.vx = (dx / dist) * 4;
                this.vy = (dy / dist) * 4;
            }

            // Random shoot (scaled by difficulty)
            if (Math.random() < 0.01 + (0.005 * this.game.level)) {
                this.shoot();
            }

        } else if (this.state === 'RETURNING') {
            // Simple homing to slot
            const dx = this.homeX - this.x;
            const dy = this.homeY - this.y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < 5) {
                this.state = 'FORMATION';
                this.vx = 0;
                this.vy = 0;
                this.diveTimer = Math.random() * 500 + 200;
            } else {
                this.x += this.vx;
                this.y += this.vy;
            }
        }
    }

    startDive() {
        this.state = 'DIVING';
        this.vy = 3 + Math.random() * 2;
        this.vx = (Math.random() - 0.5) * 2;
    }

    shoot() {
        this.game.bullets.push(new Bullet(
            this.x + this.width / 2,
            this.y + this.height,
            5,
            CONSTANTS.COLOR_NEON_RED,
            false // Enemy bullet
        ));
    }

    draw(ctx) {
        ctx.drawImage(this.sprite, this.x, this.y, this.width, this.height);
    }
}

export class PowerUp {
    constructor(x, y, type) {
        this.x = x;
        this.y = y;
        this.type = type; // 'HEART', 'SHIELD', 'TRIPLE'
        this.width = 20;
        this.height = 20;
        this.markedForDeletion = false;
        this.vy = 2;
    }

    update() {
        this.y += this.vy;
        if (this.y > CONSTANTS.SCREEN_HEIGHT) this.markedForDeletion = true;
    }

    draw(ctx) {
        ctx.font = '20px sans-serif';
        let char = '?';
        let color = '#fff';

        switch (this.type) {
            case 'HEART': char = '❤️'; break;
            case 'SHIELD': char = '🛡️'; break;
            case 'TRIPLE': char = '⚡'; break; // Triple shot
            case 'WINGMEN': char = '✈️'; break;
        }

        ctx.fillText(char, this.x, this.y + 20);
    }
}

export class Particle {
    constructor(x, y, vx, vy, color, life) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.color = color;
        this.life = life;
        this.maxLife = life;
        this.markedForDeletion = false;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life--;
        if (this.life <= 0) this.markedForDeletion = true;
    }

    draw(ctx) {
        ctx.globalAlpha = this.life / this.maxLife;
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, 2, 2);
        ctx.globalAlpha = 1;
    }
}
