export const CONSTANTS = {
    SCREEN_WIDTH: 600,
    SCREEN_HEIGHT: 800,
    FPS: 60,

    // Colors
    COLOR_NEON_BLUE: '#00f3ff',
    COLOR_NEON_PINK: '#ff00ff',
    COLOR_NEON_GREEN: '#0aff00',
    COLOR_NEON_RED: '#ff0000',

    // Game States
    STATE_MENU: 'MENU',
    STATE_PLAYING: 'PLAYING',
    STATE_GAMEOVER: 'GAMEOVER',

    // Player
    PLAYER_SPEED: 5,
    PLAYER_WIDTH: 32,
    PLAYER_HEIGHT: 32,
    PLAYER_SHOOT_DELAY: 15, // Frames

    // Enemy
    ENEMY_WIDTH: 24,
    ENEMY_HEIGHT: 24,
    ENEMY_ROWS: 4,
    ENEMY_COLS: 8,
    ENEMY_COLS_MOBILE: 6,

    // Scoring
    SCORE_KILL: 100,
    SCORE_DIVE_KILL: 200,

    // Key Codes
    KEYS: {
        LEFT: ['ArrowLeft', 'KeyA'],
        RIGHT: ['ArrowRight', 'KeyD'],
        SHOOT: ['Space', 'Enter', 'Click'] // Click handled separately
    }
};
