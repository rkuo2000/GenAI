export class SoundManager {
    constructor() {
        this.ctx = new (window.AudioContext || window.webkitAudioContext)();
        this.masterGain = this.ctx.createGain();
        this.masterGain.connect(this.ctx.destination);
        this.masterGain.gain.value = 0.3; // Default volume

        this.enabled = false;

        // Resume context on user interaction
        ['click', 'touchstart', 'keydown'].forEach(evt => {
            window.addEventListener(evt, () => this.resume(), { once: true });
        });
    }

    resume() {
        if (this.ctx.state === 'suspended') {
            this.ctx.resume().then(() => {
                this.enabled = true;
                console.log("Audio Context Resumed");
            });
        } else {
            this.enabled = true;
        }
    }

    playOscillator(type, startFreq, endFreq, duration, vol = 1) {
        if (!this.enabled) return;

        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = type;
        osc.frequency.setValueAtTime(startFreq, this.ctx.currentTime);
        if (endFreq) {
            osc.frequency.exponentialRampToValueAtTime(endFreq, this.ctx.currentTime + duration);
        }

        gain.gain.setValueAtTime(vol, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + duration);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start();
        osc.stop(this.ctx.currentTime + duration);
    }

    playShoot() {
        // High pitched "Pew"
        this.playOscillator('square', 800, 300, 0.15, 0.5);
    }

    playEnemyHit() {
        // Short noise-like pop
        this.playOscillator('sawtooth', 200, 50, 0.1, 0.4);
    }

    playExplosion() {
        // Low rumbles
        this.playOscillator('sawtooth', 100, 10, 0.4, 0.6);
        this.playOscillator('square', 80, 5, 0.3, 0.6);
    }

    playPowerUp() {
        // Rising chime
        this.playOscillator('sine', 400, 800, 0.3, 0.5);
        setTimeout(() => this.playOscillator('sine', 800, 1200, 0.3, 0.5), 150);
    }

    startMusic(bpm = 120) {
        if (!this.enabled || this.isPlayingMusic) return;
        this.isPlayingMusic = true;

        const noteDuration = 60 / bpm;
        this.nextNoteTime = this.ctx.currentTime;
        this.noteIndex = 0;

        // Simple bassline pattern (E2, E2, G2, A2)
        const freqs = [82.41, 82.41, 98.00, 110.00];

        const scheduler = () => {
            if (!this.isPlayingMusic) return;

            while (this.nextNoteTime < this.ctx.currentTime + 0.1) {
                const freq = freqs[this.noteIndex % freqs.length];
                this.playOscillator('triangle', freq, freq, 0.1, 0.2);
                this.nextNoteTime += noteDuration;
                this.noteIndex++;
            }
            this.timerID = requestAnimationFrame(scheduler);
        };

        scheduler();
    }

    stopMusic() {
        this.isPlayingMusic = false;
        if (this.timerID) cancelAnimationFrame(this.timerID);
    }
}
