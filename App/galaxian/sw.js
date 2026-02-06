const CACHE_NAME = 'galaxian-v1';
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './game.js',
  './js/constants.js',
  './js/input.js',
  './js/audio.js',
  './js/entities.js',
  './js/starfield.js'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => response || fetch(e.request))
  );
});
