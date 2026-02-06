import { CONSTANTS } from './constants.js';

export class Starfield {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.stars = [];
        this.numStars = 100;
        this.speed = 2;
        this.nebulaOffset = 0;

        this.init();
    }

    init() {
        for (let i = 0; i < this.numStars; i++) {
            this.stars.push(this.createStar(true));
        }
    }

    createStar(randomY = false) {
        return {
            x: Math.random() * this.canvas.width,
            y: randomY ? Math.random() * this.canvas.height : 0,
            z: Math.random() * 2 + 0.5, // Depth factor for parallax
            size: Math.random() * 1.5,
            color: Math.random() > 0.8 ? CONSTANTS.COLOR_NEON_BLUE : '#ffffff'
        };
    }

    update() {
        // Update Stars
        this.stars.forEach(star => {
            star.y += this.speed * star.z;
            if (star.y > this.canvas.height) {
                Object.assign(star, this.createStar());
            }
        });

        // Nebula movement
        this.nebulaOffset += 0.5;
    }

    draw() {
        // Draw Nebula (Procedural Gradient overlay)
        const gradient = this.ctx.createLinearGradient(0, this.canvas.height, 0, 0);
        gradient.addColorStop(0, '#050510');
        gradient.addColorStop(1, '#000000');

        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw faint nebula clouds (using composite operations for glow)
        this.ctx.save();
        this.ctx.globalCompositeOperation = 'screen';
        this.ctx.globalAlpha = 0.2;
        // Simple procedural nebula representation using circles/gradients could go here
        // For now, a subtle vertical gradient shift
        this.ctx.restore();

        // Draw Stars
        this.stars.forEach(star => {
            this.ctx.fillStyle = star.color;
            this.ctx.globalAlpha = Math.min(1, star.z * 0.5);
            this.ctx.beginPath();
            this.ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            this.ctx.fill();
        });
        this.ctx.globalAlpha = 1;
    }
}
