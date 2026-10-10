# Zelvo

Her gün yeni bulmacalar: Parola, Gruplanmış, Mini Çapraz, Sudoku, Kelime Avı, Kriptogram, Merdiven, Anagram ve Hedef Sayı. Her bulmacada Kolay, Orta ve Zor seviye var.

- Adres: https://nalvuran.github.io/zelvo/
- Giriş: Google ile (Firebase Authentication)
- Hesap verisi: Cloud Firestore (`users/{uid}`), kurallar `firestore.rules` dosyasında
- Telefona eklemek: tarayıcıda aç, Paylaş > Ana Ekrana Ekle

## Dosyalar

| Dosya | İçerik |
| --- | --- |
| `index.html` | Uygulamanın kendisi |
| `content.js` | Kelime listeleri (içerik eklemek için bu dosya düzenlenir) |
| `sw.js`, `manifest.webmanifest`, `icons/` | Ana ekrana ekleme ve internetsiz açılma (PWA) |
| `firestore.rules` | Veritabanı güvenlik kuralları |

Firebase sürümü: 12.19.0
