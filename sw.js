const CACHE_NAME = 'meetang88-v1';
const urlsToCache = [
  'https://meetang88th.com/login',
  'https://meetang88th.com/'
];

// ติดตั้ง Service Worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('เปิด cache แล้ว');
        return cache.addAll(urlsToCache);
      })
  );
  self.skipWaiting();
});

// ลบ cache เก่า
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('ลบ cache เก่า:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  return self.clients.claim();
});

// ดักจับ request
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // ถ้ามีใน cache ให้ใช้จาก cache
        if (response) {
          return response;
        }
        // ถ้าไม่มีให้ดึงจาก network
        return fetch(event.request);
      })
  );
});