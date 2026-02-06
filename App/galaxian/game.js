/**
 * GALAXIAN - NEON RETRO EDITION
 * 完整的游戏引擎和逻辑
 */

// ===== 游戏配置 =====
const CONFIG = {
    MAX_LEVELS: 50,
    INITIAL_LIVES: 3,
    INITIAL_SHIELD: 0,
    PLAYER_SPEED: 7,
    BULLET_SPEED: 12,
    ENEMY_BULLET_SPEED: 5,
    SHIELD_DURATION: 3000, // 毫秒
    TRIPLE_SHOT_DURATION: 15000, // 毫秒
    WINGMAN_DURATION: 20000, // 毫秒
    POWERUP_CHANCE: 0.15, // 15%概率掉落道具
    HIGH_SCORE_KEY: 'galaxian_highscores',
    STAR_COUNT: 100,
    PARTICLE_COUNT: 50
};

// ===== 音效管理器 =====
class SoundManager {
    constructor() {
        this.audioContext = null;
        this.enabled = true;
        this.musicEnabled = true;
        this.init();
    }

    init() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        } catch (e) {
            console.warn('Web Audio API not supported');
        }
    }

    resume() {
        if (this.audioContext && this.audioContext.state === 'suspended') {
            this.audioContext.resume();
        }
    }

    playTone(frequency, duration, type = 'square', volume = 0.3) {
        if (!this.enabled || !this.audioContext) return;

        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
        oscillator.type = type;

        gainNode.gain.setValueAtTime(volume, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + duration);

        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + duration);
    }

    playShoot() {
        this.playTone(880, 0.1, 'square', 0.2);
        setTimeout(() => this.playTone(1100, 0.05, 'square', 0.15), 50);
    }

    playEnemyShoot() {
        this.playTone(220, 0.15, 'sawtooth', 0.15);
    }

    playExplosion() {
        const now = this.audioContext.currentTime;
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                const freq = 100 + Math.random() * 200;
                this.playTone(freq, 0.2, 'sawtooth', 0.3);
            }, i * 30);
        }
    }

    playPowerup() {
        const notes = [523, 659, 784, 1047];
        notes.forEach((freq, i) => {
            setTimeout(() => this.playTone(freq, 0.15, 'sine', 0.3), i * 100);
        });
    }

    playShield() {
        this.playTone(440, 0.3, 'sine', 0.3);
        setTimeout(() => this.playTone(554, 0.3, 'sine', 0.3), 100);
        setTimeout(() => this.playTone(659, 0.4, 'sine', 0.3), 200);
    }

    playLevelComplete() {
        const melody = [523, 659, 784, 1047, 784, 1047];
        melody.forEach((freq, i) => {
            setTimeout(() => this.playTone(freq, 0.3, 'square', 0.25), i * 200);
        });
    }

    playGameOver() {
        const melody = [523, 494, 466, 440, 415, 392];
        melody.forEach((freq, i) => {
            setTimeout(() => this.playTone(freq, 0.4, 'sawtooth', 0.3), i * 300);
        });
    }

    playBackgroundMusic() {
        if (!this.musicEnabled || !this.audioContext) return;
        
        // 简单的低音循环
        const bassLoop = () => {
            if (!this.musicEnabled) return;
            const now = this.audioContext.currentTime;
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();
            
            osc.connect(gain);
            gain.connect(this.audioContext.destination);
            
            osc.frequency.setValueAtTime(65.41, now); // C2
            osc.type = 'sawtooth';
            gain.gain.setValueAtTime(0.05, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);
            
            osc.start(now);
            osc.stop(now + 0.5);
            
            setTimeout(() => bassLoop(), 500);
        };
        
        bassLoop();
    }

    toggleMute() {
        this.enabled = !this.enabled;
        return this.enabled;
    }

    toggleMusic() {
        this.musicEnabled = !this.musicEnabled;
        return this.musicEnabled;
    }
}

// ===== 向量工具类 =====
class Vector2 {
    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    add(v) {
        return new Vector2(this.x + v.x, this.y + v.y);
    }

    multiply(scalar) {
        return new Vector2(this.x * scalar, this.y * scalar);
    }

    distance(v) {
        return Math.sqrt((this.x - v.x) ** 2 + (this.y - v.y) ** 2);
    }
}

// ===== 粒子系统 =====
class Particle {
    constructor(x, y, color, speed, life) {
        this.x = x;
        this.y = y;
        this.vx = (Math.random() - 0.5) * speed;
        this.vy = (Math.random() - 0.5) * speed;
        this.color = color;
        this.life = life;
        this.maxLife = life;
        this.size = Math.random() * 3 + 1;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life--;
        this.size *= 0.98;
    }

    draw(ctx) {
        const alpha = this.life / this.maxLife;
        ctx.globalAlpha = alpha;
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1;
    }
}

// ===== 星星背景 =====
class Star {
    constructor(canvasWidth, canvasHeight) {
        this.x = Math.random() * canvasWidth;
        this.y = Math.random() * canvasHeight;
        this.size = Math.random() * 2;
        this.speed = Math.random() * 0.5 + 0.1;
        this.brightness = Math.random();
        this.twinkleSpeed = Math.random() * 0.05 + 0.01;
    }

    update(canvasHeight) {
        this.y += this.speed;
        if (this.y > canvasHeight) {
            this.y = 0;
            this.x = Math.random() * window.innerWidth;
        }
        this.brightness += this.twinkleSpeed;
        if (this.brightness > 1 || this.brightness < 0.3) {
            this.twinkleSpeed = -this.twinkleSpeed;
        }
    }

    draw(ctx) {
        ctx.globalAlpha = this.brightness;
        ctx.fillStyle = '#fff';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1;
    }
}

// ===== 游戏对象基类 =====
class GameObject {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.active = true;
    }

    getBounds() {
        return {
            left: this.x - this.width / 2,
            right: this.x + this.width / 2,
            top: this.y - this.height / 2,
            bottom: this.y + this.height / 2
        };
    }

    checkCollision(other) {
        const a = this.getBounds();
        const b = other.getBounds();
        return a.left < b.right && a.right > b.left && 
               a.top < b.bottom && a.bottom > b.top;
    }

    drawPixelRect(ctx, color) {
        ctx.fillStyle = color;
        const pixelSize = 3;
        const cols = Math.floor(this.width / pixelSize);
        const rows = Math.floor(this.height / pixelSize);
        
        for (let i = 0; i < cols; i++) {
            for (let j = 0; j < rows; j++) {
                if (Math.random() > 0.1) {
                    ctx.fillRect(
                        this.x - this.width/2 + i * pixelSize,
                        this.y - this.height/2 + j * pixelSize,
                        pixelSize - 0.5,
                        pixelSize - 0.5
                    );
                }
            }
        }
    }
}

// ===== 玩家飞船 =====
class Player extends GameObject {
    constructor(x, y) {
        super(x, y, 40, 40);
        this.speed = CONFIG.PLAYER_SPEED;
        this.shieldActive = false;
        this.shieldCharges = CONFIG.INITIAL_SHIELD;
        this.tripleShotActive = false;
        this.tripleShotTimer = 0;
        this.wingmanActive = false;
        this.wingmanTimer = 0;
        this.lastShotTime = 0;
        this.shootCooldown = 200; // 毫秒
        this.trailTimer = 0;
    }

    update(input, canvasWidth, deltaTime) {
        // 移动
        if (input.keys.ArrowLeft || input.keys.a) {
            this.x -= this.speed;
        }
        if (input.keys.ArrowRight || input.keys.d) {
            this.x += this.speed;
        }

        // 鼠标/触摸控制
        if (input.mouse.x !== null) {
            const targetX = input.mouse.x;
            const diff = targetX - this.x;
            this.x += diff * 0.15;
        }

        // 边界限制
        this.x = Math.max(this.width/2, Math.min(canvasWidth - this.width/2, this.x));

        // 护盾计时器
        if (this.shieldActive) {
            this.shieldTimer -= deltaTime;
            if (this.shieldTimer <= 0) {
                this.shieldActive = false;
            }
        }

        // 三连发射击计时器
        if (this.tripleShotActive) {
            this.tripleShotTimer -= deltaTime;
            if (this.tripleShotTimer <= 0) {
                this.tripleShotActive = false;
            }
        }

        // 僚机计时器
        if (this.wingmanActive) {
            this.wingmanTimer -= deltaTime;
            if (this.wingmanTimer <= 0) {
                this.wingmanActive = false;
            }
        }

        // 喷射尾迹
        this.trailTimer += deltaTime;
    }

    canShoot(currentTime) {
        return currentTime - this.lastShotTime >= this.shootCooldown;
    }

    shoot(currentTime) {
        this.lastShotTime = currentTime;
        const bullets = [];

        if (this.tripleShotActive) {
            // 三连发
            bullets.push(new Bullet(this.x, this.y - 20, 0, -CONFIG.BULLET_SPEED, 'player'));
            bullets.push(new Bullet(this.x - 15, this.y - 15, -2, -CONFIG.BULLET_SPEED + 1, 'player'));
            bullets.push(new Bullet(this.x + 15, this.y - 15, 2, -CONFIG.BULLET_SPEED + 1, 'player'));
        } else {
            bullets.push(new Bullet(this.x, this.y - 20, 0, -CONFIG.BULLET_SPEED, 'player'));
        }

        // 僚机射击
        if (this.wingmanActive) {
            bullets.push(new Bullet(this.x - 35, this.y, 0, -CONFIG.BULLET_SPEED, 'player'));
            bullets.push(new Bullet(this.x + 35, this.y, 0, -CONFIG.BULLET_SPEED, 'player'));
        }

        return bullets;
    }

    activateShield() {
        if (this.shieldCharges > 0 && !this.shieldActive) {
            this.shieldCharges--;
            this.shieldActive = true;
            this.shieldTimer = CONFIG.SHIELD_DURATION;
            return true;
        }
        return false;
    }

    activateTripleShot() {
        this.tripleShotActive = true;
        this.tripleShotTimer = CONFIG.TRIPLE_SHOT_DURATION;
    }

    activateWingman() {
        this.wingmanActive = true;
        this.wingmanTimer = CONFIG.WINGMAN_DURATION;
    }

    addShieldCharge() {
        this.shieldCharges += 2;
    }

    draw(ctx) {
        // 绘制喷射尾迹
        if (this.trailTimer % 50 < 25) {
            for (let i = 0; i < 3; i++) {
                const size = Math.random() * 4 + 2;
                ctx.fillStyle = `rgba(0, 255, 255, ${Math.random() * 0.5 + 0.3})`;
                ctx.fillRect(
                    this.x - 5 + Math.random() * 10 - size/2,
                    this.y + 20 + Math.random() * 10,
                    size,
                    size * 2
                );
            }
        }

        // 绘制护盾
        if (this.shieldActive) {
            const pulse = Math.sin(Date.now() / 100) * 0.2 + 0.8;
            ctx.strokeStyle = `rgba(0, 255, 255, ${pulse})`;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(this.x, this.y, 30, 0, Math.PI * 2);
            ctx.stroke();
            
            // 护盾光晕
            ctx.fillStyle = `rgba(0, 255, 255, ${0.1 * pulse})`;
            ctx.beginPath();
            ctx.arc(this.x, this.y, 30, 0, Math.PI * 2);
            ctx.fill();
        }

        // 绘制僚机
        if (this.wingmanActive) {
            this.drawWingman(ctx, this.x - 35, this.y + 10);
            this.drawWingman(ctx, this.x + 35, this.y + 10);
        }

        // 绘制玩家飞船（8-bit像素风格）
        this.drawShip(ctx);
    }

    drawWingman(ctx, x, y) {
        ctx.fillStyle = '#0ff';
        const pixelSize = 2;
        const wingmanPixels = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ];
        
        for (let row = 0; row < wingmanPixels.length; row++) {
            for (let col = 0; col < wingmanPixels[row].length; col++) {
                if (wingmanPixels[row][col]) {
                    ctx.fillRect(
                        x + (col - 2) * pixelSize * 2,
                        y + row * pixelSize * 2,
                        pixelSize * 2,
                        pixelSize * 2
                    );
                }
            }
        }
    }

    drawShip(ctx) {
        ctx.fillStyle = '#0ff';
        const pixelSize = 3;
        
        // 8-bit像素飞船图案
        const shipPixels = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 0]
        ];

        const offsetX = this.x - (shipPixels[0].length * pixelSize) / 2;
        const offsetY = this.y - (shipPixels.length * pixelSize) / 2;

        for (let row = 0; row < shipPixels.length; row++) {
            for (let col = 0; col < shipPixels[row].length; col++) {
                if (shipPixels[row][col]) {
                    // 添加霓虹发光效果
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = '#0ff';
                    ctx.fillRect(
                        offsetX + col * pixelSize,
                        offsetY + row * pixelSize,
                        pixelSize,
                        pixelSize
                    );
                    ctx.shadowBlur = 0;
                }
            }
        }
    }
}

// ===== 子弹 =====
class Bullet extends GameObject {
    constructor(x, y, vx, vy, type) {
        super(x, y, 6, 12);
        this.vx = vx;
        this.vy = vy;
        this.type = type; // 'player' 或 'enemy'
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;

        // 检查是否超出屏幕
        if (this.y < -20 || this.y > window.innerHeight + 20) {
            this.active = false;
        }
    }

    draw(ctx) {
        ctx.fillStyle = this.type === 'player' ? '#0ff' : '#ff0';
        ctx.shadowBlur = 10;
        ctx.shadowColor = ctx.fillStyle;
        
        // 像素风格子弹
        ctx.fillRect(this.x - 2, this.y - 6, 4, 12);
        
        ctx.shadowBlur = 0;
    }
}

// ===== 敌人 =====
class Enemy extends GameObject {
    constructor(x, y, type, row, col) {
        super(x, y, 35, 35);
        this.type = type; // 0=普通, 1=快速, 2=坦克
        this.row = row;
        this.col = col;
        this.baseX = x;
        this.baseY = y;
        this.angle = 0;
        this.formationX = x;
        this.formationY = y;
        this.isAttacking = false;
        this.attackSpeed = 2 + Math.random() * 2;
        this.hits = 0;
        this.maxHits = type === 2 ? 3 : 1;
        this.flashTime = 0;
        this.lastShotTime = 0;
        this.shootCooldown = 3000 + Math.random() * 2000;
    }

    update(formationOffsetX, formationOffsetY, canvasWidth, canvasHeight, 
           playerX, playerY, deltaTime, level) {
        // 闪烁效果
        if (this.flashTime > 0) {
            this.flashTime -= deltaTime;
        }

        // 移动模式
        if (this.isAttacking) {
            // 攻击模式：追踪玩家
            const dx = playerX - this.x;
            const dy = playerY - this.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            
            if (dist > 0) {
                this.x += (dx / dist) * this.attackSpeed;
                this.y += (dy / dist) * this.attackSpeed;
            }

            // 垂直循环
            if (this.y > canvasHeight + 50) {
                this.y = -50;
                this.x = Math.random() * canvasWidth;
            }

            // 随机返回阵型
            if (Math.random() < 0.005 && this.y > canvasHeight * 0.6) {
                this.isAttacking = false;
            }
        } else {
            // 阵型模式
            const targetX = this.formationX + formationOffsetX;
            const targetY = this.formationY + formationOffsetY;
            
            this.x += (targetX - this.x) * 0.1;
            this.y += (targetY - this.y) * 0.1;

            // 随等级增加的摆动
            this.angle += 0.05 + level * 0.005;
            this.x += Math.sin(this.angle + this.col * 0.5) * (0.5 + level * 0.1);
        }

        // 射击逻辑
        const now = Date.now();
        if (now - this.lastShotTime > this.shootCooldown) {
            this.lastShotTime = now;
            // 只有攻击中的敌人和最下排敌人才会射击
            if (this.isAttacking || this.row === 3) {
                return this.shoot();
            }
        }

        return null;
    }

    shoot() {
        return new Bullet(this.x, this.y + 20, 0, CONFIG.ENEMY_BULLET_SPEED, 'enemy');
    }

    hit() {
        this.hits++;
        this.flashTime = 200;
        return this.hits >= this.maxHits;
    }

    startAttack() {
        this.isAttacking = true;
    }

    draw(ctx) {
        // 击中闪烁
        if (this.flashTime > 0) {
            ctx.fillStyle = '#fff';
            ctx.fillRect(this.x - this.width/2 - 5, this.y - this.height/2 - 5, 
                        this.width + 10, this.height + 10);
        }

        // 根据类型绘制不同的敌人
        switch(this.type) {
            case 0: // 普通敌人
                this.drawEnemyType0(ctx);
                break;
            case 1: // 快速敌人
                this.drawEnemyType1(ctx);
                break;
            case 2: // 坦克敌人
                this.drawEnemyType2(ctx);
                break;
        }
    }

    drawEnemyType0(ctx) {
        // 经典Galaxian风格敌人
        const colors = ['#ff0000', '#ff6600'];
        ctx.fillStyle = colors[this.hits] || colors[0];
        
        const pixelSize = 2;
        const pixels = [
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1]
        ];

        this.drawPixels(ctx, pixels, pixelSize, ctx.fillStyle);
    }

    drawEnemyType1(ctx) {
        // 快速敌人 - 蓝色
        ctx.fillStyle = '#00ffff';
        
        const pixelSize = 2;
        const pixels = [
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0]
        ];

        this.drawPixels(ctx, pixels, pixelSize, ctx.fillStyle);
    }

    drawEnemyType2(ctx) {
        // 坦克敌人 - 紫色
        ctx.fillStyle = '#ff00ff';
        
        const pixelSize = 2;
        const pixels = [
            [0, 1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1]
        ];

        this.drawPixels(ctx, pixels, pixelSize, ctx.fillStyle);

        // 坦克敌人血条
        if (this.maxHits > 1) {
            const barWidth = 30;
            const barHeight = 4;
            ctx.fillStyle = '#333';
            ctx.fillRect(this.x - barWidth/2, this.y - this.height/2 - 10, barWidth, barHeight);
            ctx.fillStyle = '#0f0';
            ctx.fillRect(this.x - barWidth/2, this.y - this.height/2 - 10, 
                        barWidth * (this.maxHits - this.hits) / this.maxHits, barHeight);
        }
    }

    drawPixels(ctx, pixels, pixelSize, color) {
        ctx.shadowBlur = 8;
        ctx.shadowColor = color;
        
        const offsetX = this.x - (pixels[0].length * pixelSize) / 2;
        const offsetY = this.y - (pixels.length * pixelSize) / 2;

        for (let row = 0; row < pixels.length; row++) {
            for (let col = 0; col < pixels[row].length; col++) {
                if (pixels[row][col]) {
                    ctx.fillRect(
                        offsetX + col * pixelSize,
                        offsetY + row * pixelSize,
                        pixelSize,
                        pixelSize
                    );
                }
            }
        }
        
        ctx.shadowBlur = 0;
    }
}

// ===== 道具 =====
class PowerUp extends GameObject {
    constructor(x, y, type) {
        super(x, y, 30, 30);
        this.type = type; // 'health', 'shield', 'triple', 'wingman'
        this.vy = 2;
        this.angle = 0;
        
        const icons = {
            'health': '❤️',
            'shield': '🛡️',
            'triple': '⚡',
            'wingman': '✈️'
        };
        this.icon = icons[type];
    }

    update() {
        this.y += this.vy;
        this.angle += 0.05;
        
        if (this.y > window.innerHeight + 50) {
            this.active = false;
        }
    }

    draw(ctx) {
        const scale = 1 + Math.sin(this.angle) * 0.1;
        
        // 光晕背景
        ctx.fillStyle = 'rgba(255, 255, 0, 0.3)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, 20 * scale, 0, Math.PI * 2);
        ctx.fill();
        
        // 绘制图标
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(this.icon, this.x, this.y);
    }
}

// ===== 游戏主类 =====
class GalaxianGame {
    constructor() {
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.soundManager = new SoundManager();
        
        // 游戏状态
        this.state = 'start'; // start, playing, paused, levelComplete, gameOver
        this.score = 0;
        this.level = 1;
        this.lives = CONFIG.INITIAL_LIVES;
        this.highScores = this.loadHighScores();
        
        // 游戏对象
        this.player = null;
        this.enemies = [];
        this.bullets = [];
        this.powerups = [];
        this.particles = [];
        this.stars = [];
        
        // 输入处理
        this.input = {
            keys: {},
            mouse: { x: null, y: null, down: false },
            touch: { x: null, y: null },
            tripleTap: { count: 0, lastTime: 0 }
        };
        
        // 动画帧
        this.lastTime = 0;
        this.animationId = null;
        
        // 敌人阵型
        this.formationOffsetX = 0;
        this.formationDirection = 1;
        
        this.init();
    }

    init() {
        this.resize();
        this.setupEventListeners();
        this.createStars();
        this.updateHighScoreDisplay();
        
        // 设置初始UI
        this.updateHUD();
        
        // 启动渲染循环
        this.lastTime = performance.now();
        this.gameLoop();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.createStars();
    }

    createStars() {
        this.stars = [];
        for (let i = 0; i < CONFIG.STAR_COUNT; i++) {
            this.stars.push(new Star(this.canvas.width, this.canvas.height));
        }
    }

    setupEventListeners() {
        // 键盘控制
        window.addEventListener('keydown', (e) => {
            this.input.keys[e.key] = true;
            
            if (this.state === 'playing') {
                if (e.code === 'Space' || e.code === 'KeyZ') {
                    this.playerShoot();
                }
                if (e.code === 'KeyX' || e.button === 2) {
                    this.activateShield();
                }
            }
            
            if (e.key === 'Escape') {
                this.togglePause();
            }
        });

        window.addEventListener('keyup', (e) => {
            this.input.keys[e.key] = false;
        });

        // 鼠标控制
        this.canvas.addEventListener('mousemove', (e) => {
            this.input.mouse.x = e.clientX;
            this.input.mouse.y = e.clientY;
        });

        this.canvas.addEventListener('mousedown', (e) => {
            if (e.button === 0) { // 左键
                this.playerShoot();
            } else if (e.button === 2) { // 右键
                e.preventDefault();
                this.activateShield();
            }
        });

        this.canvas.addEventListener('contextmenu', (e) => {
            e.preventDefault();
        });

        this.canvas.addEventListener('mouseleave', () => {
            this.input.mouse.x = null;
            this.input.mouse.y = null;
        });

        // 触摸控制
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            this.input.touch.x = touch.clientX;
            this.input.touch.y = touch.clientY;
            
            // 检测三击护盾
            const now = Date.now();
            if (now - this.input.tripleTap.lastTime < 750) {
                this.input.tripleTap.count++;
                if (this.input.tripleTap.count >= 3) {
                    this.activateShield();
                    this.input.tripleTap.count = 0;
                }
            } else {
                this.input.tripleTap.count = 1;
            }
            this.input.tripleTap.lastTime = now;
            
            // 自动射击
            this.playerShoot();
        }, { passive: false });

        this.canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            this.input.mouse.x = touch.clientX;
            this.input.mouse.y = touch.clientY;
        }, { passive: false });

        this.canvas.addEventListener('touchend', (e) => {
            e.preventDefault();
            this.input.mouse.x = null;
            this.input.mouse.y = null;
        });

        // 窗口调整
        window.addEventListener('resize', () => this.resize());

        // UI按钮
        document.getElementById('start-btn').addEventListener('click', () => this.startGame());
        document.getElementById('restart-btn').addEventListener('click', () => this.restartGame());
        document.getElementById('menu-btn').addEventListener('click', () => this.showMainMenu());
        document.getElementById('next-level-btn').addEventListener('click', () => this.nextLevel());
        document.getElementById('high-score-btn').addEventListener('click', () => this.showHighScores());
        document.getElementById('close-high-score').addEventListener('click', () => this.hideHighScores());
        document.getElementById('mute-btn').addEventListener('click', () => this.toggleMute());
        document.getElementById('music-btn').addEventListener('click', () => this.toggleMusic());
        document.getElementById('pause-btn').addEventListener('click', () => this.togglePause());
    }

    startGame() {
        this.soundManager.resume();
        this.soundManager.playBackgroundMusic();
        
        this.state = 'playing';
        this.score = 0;
        this.level = 1;
        this.lives = CONFIG.INITIAL_LIVES;
        
        document.getElementById('start-screen').classList.add('hidden');
        document.getElementById('game-over-screen').classList.add('hidden');
        document.getElementById('pause-btn').classList.remove('hidden');
        
        this.startLevel();
        this.updateHUD();
    }

    restartGame() {
        this.startGame();
    }

    showMainMenu() {
        this.state = 'start';
        document.getElementById('game-over-screen').classList.add('hidden');
        document.getElementById('start-screen').classList.remove('hidden');
        document.getElementById('pause-btn').classList.add('hidden');
        this.enemies = [];
        this.bullets = [];
        this.powerups = [];
    }

    startLevel() {
        // 创建玩家
        this.player = new Player(this.canvas.width / 2, this.canvas.height - 100);
        
        // 创建敌人阵型
        this.createEnemyFormation();
        
        // 清除之前的子弹和道具
        this.bullets = [];
        this.powerups = [];
        
        this.updateHUD();
    }

    createEnemyFormation() {
        this.enemies = [];
        
        // 根据屏幕大小决定列数
        const isMobile = window.innerWidth <= 768;
        const cols = isMobile ? 6 : 10;
        const rows = 4;
        const spacingX = isMobile ? 45 : 55;
        const spacingY = 45;
        
        const totalWidth = (cols - 1) * spacingX;
        const startX = (this.canvas.width - totalWidth) / 2;
        const startY = 80 + (this.level - 1) * 5; // 随等级向下移动
        
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                let type = 0; // 默认普通
                if (row === 0) type = 2; // 第一排坦克
                else if (row === 1) type = 1; // 第二排快速
                
                const enemy = new Enemy(
                    startX + col * spacingX,
                    startY + row * spacingY,
                    type,
                    row,
                    col
                );
                
                enemy.formationX = enemy.x;
                enemy.formationY = enemy.y;
                
                this.enemies.push(enemy);
            }
        }
    }

    playerShoot() {
        if (this.state !== 'playing' || !this.player) return;
        
        const now = Date.now();
        if (this.player.canShoot(now)) {
            const bullets = this.player.shoot(now);
            this.bullets.push(...bullets);
            this.soundManager.playShoot();
        }
    }

    activateShield() {
        if (this.state !== 'playing' || !this.player) return;
        
        if (this.player.activateShield()) {
            this.soundManager.playShield();
            this.updateHUD();
        }
    }

    togglePause() {
        if (this.state === 'playing') {
            this.state = 'paused';
            document.getElementById('pause-btn').textContent = '▶️';
        } else if (this.state === 'paused') {
            this.state = 'playing';
            document.getElementById('pause-btn').textContent = '⏸️';
            this.lastTime = performance.now();
        }
    }

    toggleMute() {
        const enabled = this.soundManager.toggleMute();
        document.getElementById('mute-btn').textContent = enabled ? '🔊' : '🔇';
        document.getElementById('mute-btn').classList.toggle('muted', !enabled);
    }

    toggleMusic() {
        const enabled = this.soundManager.toggleMusic();
        document.getElementById('music-btn').classList.toggle('muted', !enabled);
    }

    update(deltaTime) {
        if (this.state !== 'playing') return;

        // 更新玩家
        this.player.update(this.input, this.canvas.width, deltaTime);

        // 更新星星背景
        this.stars.forEach(star => star.update(this.canvas.height));

        // 更新粒子
        this.particles = this.particles.filter(p => {
            p.update();
            return p.life > 0;
        });

        // 敌人阵型移动
        this.formationOffsetX += this.formationDirection * (0.5 + this.level * 0.1);
        const formationLimit = 50;
        if (Math.abs(this.formationOffsetX) > formationLimit) {
            this.formationDirection *= -1;
        }

        // 自动置中
        if (this.enemies.length > 0 && !this.enemies.some(e => e.isAttacking)) {
            const centerX = this.canvas.width / 2;
            const enemyCenterX = this.enemies.reduce((sum, e) => sum + e.formationX, 0) / this.enemies.length;
            const drift = centerX - enemyCenterX;
            this.enemies.forEach(e => {
                e.formationX += drift * 0.01;
            });
        }

        // 更新敌人
        this.enemies.forEach(enemy => {
            const bullet = enemy.update(
                this.formationOffsetX, 0,
                this.canvas.width, this.canvas.height,
                this.player.x, this.player.y,
                deltaTime, this.level
            );
            
            if (bullet) {
                this.bullets.push(bullet);
                this.soundManager.playEnemyShoot();
            }
        });

        // 随机敌人攻击
        if (Math.random() < 0.005 + this.level * 0.001) {
            const availableEnemies = this.enemies.filter(e => !e.isAttacking);
            if (availableEnemies.length > 0) {
                const attacker = availableEnemies[Math.floor(Math.random() * availableEnemies.length)];
                attacker.startAttack();
            }
        }

        // 更新子弹
        this.bullets = this.bullets.filter(bullet => {
            bullet.update();
            return bullet.active;
        });

        // 更新道具
        this.powerups = this.powerups.filter(powerup => {
            powerup.update();
            return powerup.active;
        });

        // 碰撞检测
        this.checkCollisions();

        // 检查关卡完成
        if (this.enemies.length === 0) {
            this.levelComplete();
        }
    }

    checkCollisions() {
        // 玩家子弹击中敌人
        this.bullets.filter(b => b.type === 'player').forEach(bullet => {
            this.enemies.forEach(enemy => {
                if (bullet.active && enemy.active && bullet.checkCollision(enemy)) {
                    bullet.active = false;
                    
                    if (enemy.hit()) {
                        // 敌人被消灭
                        enemy.active = false;
                        this.score += (enemy.type + 1) * 100;
                        this.createExplosion(enemy.x, enemy.y, enemy.type);
                        this.soundManager.playExplosion();
                        
                        // 掉落道具
                        if (Math.random() < CONFIG.POWERUP_CHANCE) {
                            this.spawnPowerUp(enemy.x, enemy.y);
                        }
                    }
                }
            });
        });

        // 敌人子弹击中玩家
        this.bullets.filter(b => b.type === 'enemy').forEach(bullet => {
            if (bullet.active && this.player.checkCollision(bullet)) {
                bullet.active = false;
                this.playerHit();
            }
        });

        // 敌人撞击玩家
        this.enemies.forEach(enemy => {
            if (enemy.active && this.player.checkCollision(enemy)) {
                enemy.active = false;
                this.createExplosion(enemy.x, enemy.y, enemy.type);
                this.playerHit();
            }
        });

        // 玩家拾取道具
        this.powerups.forEach(powerup => {
            if (powerup.active && this.player.checkCollision(powerup)) {
                powerup.active = false;
                this.collectPowerUp(powerup.type);
            }
        });

        // 清理非活动对象
        this.enemies = this.enemies.filter(e => e.active);
        this.bullets = this.bullets.filter(b => b.active);
        this.powerups = this.powerups.filter(p => p.active);
    }

    playerHit() {
        if (this.player.shieldActive) {
            this.player.shieldActive = false;
            this.soundManager.playShield();
            this.createExplosion(this.player.x, this.player.y, 0, '#0ff');
        } else {
            this.lives--;
            this.createExplosion(this.player.x, this.player.y, 0, '#f00');
            this.soundManager.playExplosion();
            
            if (this.lives <= 0) {
                this.gameOver();
            } else {
                // 短暂无敌时间
                this.player.x = this.canvas.width / 2;
            }
        }
        this.updateHUD();
    }

    spawnPowerUp(x, y) {
        const types = ['health', 'shield', 'triple', 'wingman'];
        const type = types[Math.floor(Math.random() * types.length)];
        this.powerups.push(new PowerUp(x, y, type));
    }

    collectPowerUp(type) {
        this.soundManager.playPowerup();
        
        const messages = {
            'health': { icon: '❤️', text: 'HEALTH UP!' },
            'shield': { icon: '🛡️', text: 'SHIELD CHARGE!' },
            'triple': { icon: '⚡', text: 'TRIPLE SHOT!' },
            'wingman': { icon: '✈️', text: 'WINGMAN READY!' }
        };
        
        const msg = messages[type];
        this.showPowerUpNotification(msg.icon, msg.text);
        
        switch(type) {
            case 'health':
                this.lives = Math.min(this.lives + 1, 5);
                break;
            case 'shield':
                this.player.addShieldCharge();
                break;
            case 'triple':
                this.player.activateTripleShot();
                break;
            case 'wingman':
                this.player.activateWingman();
                break;
        }
        
        this.updateHUD();
    }

    showPowerUpNotification(icon, text) {
        const notify = document.getElementById('powerup-notify');
        document.getElementById('powerup-icon').textContent = icon;
        document.getElementById('powerup-text').textContent = text;
        notify.classList.remove('hidden');
        
        setTimeout(() => {
            notify.classList.add('hidden');
        }, 2000);
    }

    createExplosion(x, y, type, color = null) {
        const colors = ['#ff6600', '#ff0000', '#ffff00'];
        const particleColor = color || colors[type] || colors[0];
        
        for (let i = 0; i < CONFIG.PARTICLE_COUNT; i++) {
            this.particles.push(new Particle(
                x, y, particleColor,
                Math.random() * 8 + 2,
                Math.random() * 30 + 20
            ));
        }
    }

    levelComplete() {
        this.state = 'levelComplete';
        this.soundManager.playLevelComplete();
        
        const bonus = this.lives * 1000 + this.player.shieldCharges * 500;
        this.score += bonus;
        
        document.getElementById('level-bonus').textContent = bonus;
        document.getElementById('level-complete-screen').classList.remove('hidden');
        
        this.updateHUD();
    }

    nextLevel() {
        document.getElementById('level-complete-screen').classList.add('hidden');
        
        if (this.level >= CONFIG.MAX_LEVELS) {
            // 通关！
            this.gameOver(true);
        } else {
            this.level++;
            this.state = 'playing';
            this.startLevel();
        }
    }

    gameOver(victory = false) {
        this.state = 'gameOver';
        this.soundManager.playGameOver();
        
        const isNewRecord = this.saveHighScore(this.score);
        
        document.getElementById('final-score').textContent = this.score;
        document.getElementById('new-record-msg').classList.toggle('hidden', !isNewRecord);
        document.getElementById('game-over-screen').classList.remove('hidden');
        document.getElementById('pause-btn').classList.add('hidden');
    }

    draw() {
        // 清空画布
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // 绘制星星
        this.stars.forEach(star => star.draw(this.ctx));

        // 绘制粒子
        this.particles.forEach(particle => particle.draw(this.ctx));

        // 绘制道具
        this.powerups.forEach(powerup => powerup.draw(this.ctx));

        // 绘制敌人
        this.enemies.forEach(enemy => enemy.draw(this.ctx));

        // 绘制子弹
        this.bullets.forEach(bullet => bullet.draw(this.ctx));

        // 绘制玩家
        if (this.player && this.state === 'playing') {
            this.player.draw(this.ctx);
        }
    }

    gameLoop() {
        const currentTime = performance.now();
        const deltaTime = currentTime - this.lastTime;
        this.lastTime = currentTime;

        this.update(deltaTime);
        this.draw();

        this.animationId = requestAnimationFrame(() => this.gameLoop());
    }

    updateHUD() {
        document.getElementById('score-display').textContent = this.score.toLocaleString();
        document.getElementById('level-display').textContent = this.level;
        document.getElementById('shield-display').textContent = this.player ? this.player.shieldCharges : 0;
        
        const hearts = '❤️'.repeat(Math.max(0, this.lives));
        document.getElementById('lives-display').textContent = hearts || '💀';
    }

    loadHighScores() {
        const saved = localStorage.getItem(CONFIG.HIGH_SCORE_KEY);
        return saved ? JSON.parse(saved) : [];
    }

    saveHighScore(score) {
        const entry = {
            score: score,
            date: new Date().toLocaleDateString(),
            level: this.level
        };
        
        this.highScores.push(entry);
        this.highScores.sort((a, b) => b.score - a.score);
        this.highScores = this.highScores.slice(0, 10);
        
        localStorage.setItem(CONFIG.HIGH_SCORE_KEY, JSON.stringify(this.highScores));
        
        return this.highScores.indexOf(entry) < 10;
    }

    showHighScores() {
        const list = document.getElementById('high-score-list');
        list.innerHTML = '';
        
        if (this.highScores.length === 0) {
            list.innerHTML = '<li style="text-align: center; color: #666;">NO RECORDS YET</li>';
        } else {
            this.highScores.forEach((entry, index) => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <span class="rank">#${index + 1}</span>
                    <span class="name">LV.${entry.level} ${entry.date}</span>
                    <span class="score">${entry.score.toLocaleString()}</span>
                `;
                list.appendChild(li);
            });
        }
        
        document.getElementById('high-score-panel').classList.remove('hidden');
    }

    hideHighScores() {
        document.getElementById('high-score-panel').classList.add('hidden');
    }

    updateHighScoreDisplay() {
        // 初始显示
    }
}

// ===== 初始化游戏 =====
window.addEventListener('load', () => {
    const game = new GalaxianGame();
    
    // 注册Service Worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js')
            .then(reg => console.log('Service Worker registered'))
            .catch(err => console.log('Service Worker registration failed'));
    }
});