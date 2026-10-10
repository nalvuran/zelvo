/* Zelvo service worker: uygulama internetsiz de açılsın diye dosyaları önbellekte tutar */
const VERSION = "zelvo-s13-20261010153523";
const SHELL = ["./", "./index.html", "./content.js?v=20261010153523", "./manifest.webmanifest", "./icons/icon-192.png", "./icons/icon-512.png", "./icons/apple-touch-icon.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const req = e.request; if (req.method !== "GET") return;
  const url = new URL(req.url);
  const sameOrigin = url.origin === self.location.origin;
  const staticCdn = url.hostname === "www.gstatic.com" && url.pathname.startsWith("/firebasejs/") || url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com";
  if (sameOrigin && req.mode === "navigate") {
    /* Sayfa: önce ağ (güncel sürüm), internet yoksa önbellek */
    e.respondWith(fetch(req, { cache: "no-cache" }).then(res => { const copy = res.clone(); caches.open(VERSION).then(c => c.put("./index.html", copy)); return res; }).catch(() => caches.match("./index.html")));
    return;
  }
  if (sameOrigin && url.pathname.endsWith("/version.json")) return; /* sürüm kontrolü her zaman ağdan */
  if (sameOrigin || staticCdn) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => { if (res.ok || res.type === "opaque") { const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); } return res; })));
  }
});
