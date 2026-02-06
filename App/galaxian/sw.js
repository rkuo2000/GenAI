/**
 * GALAXIAN Service Worker
 * 提供离线游戏支持和资源缓存
 */

const CACHE_NAME = 'galaxian-v1';
const STATIC_ASSETS = [
    './',
    './index.html',
    './styles.css',
    './game.js',
    './manifest.json',
    'https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'
];

// 安装时缓存静态资源
self.addEventListener('install', event => {
    console.log('[SW] Installing...');
    
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('[SW] Caching static assets');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => {
                console.log('[SW] Installation complete');
                return self.skipWaiting();
            })
            .catch(err => {
                console.error('[SW] Cache failed:', err);
            })
    );
});

// 激活时清理旧缓存
self.addEventListener('activate', event => {
    console.log('[SW] Activating...');
    
    event.waitUntil(
        caches.keys()
            .then(cacheNames => {
                return Promise.all(
                    cacheNames
                        .filter(name => name !== CACHE_NAME)
                        .map(name => {
                            console.log('[SW] Deleting old cache:', name);
                            return caches.delete(name);
                        })
                );
            })
            .then(() => {
                console.log('[SW] Activation complete');
                return self.clients.claim();
            })
    );
});

// 拦截网络请求
self.addEventListener('fetch', event => {
    const { request } = event;
    
    // 跳过非GET请求
    if (request.method !== 'GET') {
        return;
    }
    
    // 策略：优先使用缓存，回退到网络
    event.respondWith(
        caches.match(request)
            .then(cachedResponse => {
                if (cachedResponse) {
                    // 返回缓存的版本
                    // 同时在后台更新缓存
                    fetch(request)
                        .then(networkResponse => {
                            if (networkResponse && networkResponse.status === 200) {
                                caches.open(CACHE_NAME)
                                    .then(cache => cache.put(request, networkResponse));
                            }
                        })
                        .catch(() => {
                            // 网络请求失败，忽略错误
                        });
                    
                    return cachedResponse;
                }
                
                // 缓存未命中，从网络获取
                return fetch(request)
                    .then(networkResponse => {
                        if (!networkResponse || networkResponse.status !== 200) {
                            return networkResponse;
                        }
                        
                        // 缓存新资源
                        const responseToCache = networkResponse.clone();
                        caches.open(CACHE_NAME)
                            .then(cache => cache.put(request, responseToCache));
                        
                        return networkResponse;
                    })
                    .catch(() => {
                        // 网络和缓存都失败
                        console.error('[SW] Fetch failed:', request.url);
                        
                        // 如果是页面请求，返回离线页面
                        if (request.mode === 'navigate') {
                            return caches.match('./index.html');
                        }
                        
                        return new Response('Offline', {
                            status: 503,
                            statusText: 'Service Unavailable'
                        });
                    });
            })
    );
});

// 处理后台同步（用于保存高分等）
self.addEventListener('sync', event => {
    if (event.tag === 'sync-highscores') {
        console.log('[SW] Syncing high scores...');
        // 可以在这里实现后台同步逻辑
    }
});

// 处理推送通知（可选）
self.addEventListener('push', event => {
    const data = event.data.json();
    
    const options = {
        body: data.body || 'New high score achieved!',
        icon: './icon-192x192.png',
        badge: './icon-72x72.png',
        vibrate: [100, 50, 100],
        data: data,
        actions: [
            {
                action: 'play',
                title: 'Play Now'
            },
            {
                action: 'close',
                title: 'Close'
            }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification('GALAXIAN', options)
    );
});

// 处理通知点击
self.addEventListener('notificationclick', event => {
    event.notification.close();
    
    if (event.action === 'play') {
        event.waitUntil(
            clients.openWindow('./')
        );
    }
});