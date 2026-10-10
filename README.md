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

## Sürüm geçmişi

Uygulamadaki sürüm numarası `surumler.json` dosyasındaki son kayıttır.

| Sürüm | Tarih | Değişiklik |
| --- | --- | --- |
| 5 | 10 Ekim 2026 | Otomatik güncelleme: uygulama açılınca ve arka plandan dönünce yeni sürümü kontrol edip kendini yeniliyor. Oyun ortasındaysan ana sayfaya dönünce yükleniyor. |
| 4 | 10 Ekim 2026 | Ana sayfadaki bulmaca kartlarından seviye yazısı kaldırıldı; kartta yalnızca bitirilen bulmacanın sonucu görünüyor. |
| 3 | 10 Ekim 2026 | Sürüm numarası eklendi: profil penceresinde ve Ayarlar'da görünüyor, son değişiklikler Ayarlar'da listeleniyor. |
| 2 | 10 Ekim 2026 | Alt menü ekranın en altına sabitlendi; iPhone'da altta kalan boşluk giderildi. |
| 1 | 10 Ekim 2026 | İlk sürüm: 9 bulmaca, Kolay/Orta/Zor seviyeler, Google ile giriş, ana ekrana eklenebilir uygulama. |
