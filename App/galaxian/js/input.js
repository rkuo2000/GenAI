import { CONSTANTS } from './constants.js';

export class InputHandler {
    constructor(canvas) {
        this.keys = {
            left: false,
            right: false,
            shoot: false
        };

        this.touchX = null;
        this.canvas = canvas;

        this.resizeScale = 1;

        // Event Listeners
        window.addEventListener('keydown', (e) => this.onKeyDown(e));
        window.addEventListener('keyup', (e) => this.onKeyUp(e));

        // Touch / Mouse for mobile & movement
        this.canvas.addEventListener('touchstart', (e) => this.onTouchStart(e), { passive: false });
        this.canvas.addEventListener('touchmove', (e) => this.onTouchMove(e), { passive: false });
        this.canvas.addEventListener('touchend', (e) => this.onTouchEnd(e));

        this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
        this.canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
        this.canvas.addEventListener('mouseup', (e) => this.onMouseUp(e));

        // Custom events for start/restart
        this.onTap = null;
    }

    setScale(scale) {
        this.resizeScale = scale;
    }

    onKeyDown(e) {
        if (CONSTANTS.KEYS.LEFT.includes(e.code) || CONSTANTS.KEYS.LEFT.includes(e.key)) this.keys.left = true;
        if (CONSTANTS.KEYS.RIGHT.includes(e.code) || CONSTANTS.KEYS.RIGHT.includes(e.key)) this.keys.right = true;
        if (CONSTANTS.KEYS.SHOOT.includes(e.code) || CONSTANTS.KEYS.SHOOT.includes(e.key)) {
            this.keys.shoot = true;
            if (this.onTap) this.onTap();
        }
    }

    onKeyUp(e) {
        if (CONSTANTS.KEYS.LEFT.includes(e.code) || CONSTANTS.KEYS.LEFT.includes(e.key)) this.keys.left = false;
        if (CONSTANTS.KEYS.RIGHT.includes(e.code) || CONSTANTS.KEYS.RIGHT.includes(e.key)) this.keys.right = false;
        if (CONSTANTS.KEYS.SHOOT.includes(e.code) || CONSTANTS.KEYS.SHOOT.includes(e.key)) this.keys.shoot = false;
    }

    // Touch Handling (Drag to move, Tap to shoot/start)
    onTouchStart(e) {
        e.preventDefault();
        const touch = e.touches[0];
        this.updateTouchPosition(touch.clientX);
        this.keys.shoot = true; // Auto-shoot on touch

        if (this.onTap) this.onTap();
    }

    onTouchMove(e) {
        e.preventDefault();
        const touch = e.touches[0];
        this.updateTouchPosition(touch.clientX);
    }

    onTouchEnd(e) {
        e.preventDefault();
        this.touchX = null;
        this.keys.left = false;
        this.keys.right = false;
        this.keys.shoot = false;
    }

    // Mouse Handling (Drag-like behavior)
    onMouseDown(e) {
        this.updateTouchPosition(e.clientX);
        this.keys.shoot = true;
        if (this.onTap) this.onTap();
    }

    onMouseMove(e) {
        if (this.keys.shoot) { // Only move if mouse is down "dragging" style or strictly follow mouse? 
            // The prompt says "Touch and Drag", usually implies relative or absolute follow. 
            // For PC mouse, "Right click" was mentioned as action, "Left Click" as shoot/move.
            // Let's stick to mouse follows horizontal position if button pressed.
            this.updateTouchPosition(e.clientX);
        }
    }

    onMouseUp(e) {
        this.touchX = null;
        this.keys.left = false;
        this.keys.right = false;
        this.keys.shoot = false;
    }

    updateTouchPosition(clientX) {
        const rect = this.canvas.getBoundingClientRect();
        // Calculate relative X position in game coordinates
        const canvasX = (clientX - rect.left) * (this.canvas.width / rect.width);

        // We'll expose the target X for the player to move towards, generic "Virtual Joystick" style
        // Or simply expose the raw X and let player Logic handle lerping.
        // For Galaxian, let's store the target X.
        this.touchX = canvasX;
    }
}
