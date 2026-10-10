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
| 16 | 10 Ekim 2026 | Bulmaca isimleri Everyday Puzzles ile aynı yapıldı: Anygram, Gizli Kelime, Hashtag, Kelime Arama, Mini Çapraz Bulmaca, Tangle. |
| 15 | 10 Ekim 2026 | Üç yeni bulmaca: Türet (harflerden kelime türet, bonus kelimeler), Sözlük (gizli kelimenin sözlükteki yerini daralt) ve Takas (harflerin yerini değiştirerek 6 kelimeyi tamamla). Hepsinde Kolay/Orta/Zor var. |
| 14 | 10 Ekim 2026 | Bulmacaya girerken önce seviye soruluyor: Kolay, Orta ve Zor için ne değiştiği yazıyor, bugün oynadıysan durumu görünüyor. Oyun içindeki seçici yerine seviye etiketi var; dokununca seviye değişir. |
| 13 | 10 Ekim 2026 | Tüm ikonlar Zuqio ikon setinin stiline geçti: çizgi stili, 24×24, çizgi kalınlığı 2, yuvarlak uçlar, tek renk. Bulmaca ikonları yeniden çizildi. |
| 12 | 10 Ekim 2026 | Alt menü inceltildi: daha az yükseklik kaplıyor ve ekranın altına daha yakın duruyor. |
| 11 | 10 Ekim 2026 | Menünün altındaki şeridin rengi düzeltildi: iPhone o alanı sayfa zemininin düz rengiyle dolduruyordu, bu renk artık menüyle aynı. Teşhis satırındaki ekran ölçüsü hatası giderildi. |
| 10 | 10 Ekim 2026 | iOS 26 ana ekran uygulamasındaki alt şerit menüyle aynı renge boyandı; şerit varken menünün alt boşluğu kısalıyor. |
| 9 | 10 Ekim 2026 | iOS 26'daki alt boşluk hatası için: uygulama açılınca pencerenin doğru ölçülmesi için kendini bir kez kaydırıyor. Sürüm 7'deki ekran boyutu ölçümü geri alındı. |
| 8 | 10 Ekim 2026 | Ayarlar'a ekran ölçüleri teşhis satırı eklendi; alt menünün altında boşluk kalırsa menüyle aynı renkte görünüyor. |
| 7 | 10 Ekim 2026 | Ana ekran uygulamasında yükseklik artık telefonun ekran boyutundan alınıyor; alt menü ilk açılışta da en altta. |
| 6 | 10 Ekim 2026 | Alt menü ilk açılışta da en altta: uygulama ekrana sabitlendi, kaydırma sadece içerikte. |
| 5 | 10 Ekim 2026 | Otomatik güncelleme: uygulama açılınca ve arka plandan dönünce yeni sürümü kontrol edip kendini yeniliyor. Oyun ortasındaysan ana sayfaya dönünce yükleniyor. |
| 4 | 10 Ekim 2026 | Ana sayfadaki bulmaca kartlarından seviye yazısı kaldırıldı; kartta yalnızca bitirilen bulmacanın sonucu görünüyor. |
| 3 | 10 Ekim 2026 | Sürüm numarası eklendi: profil penceresinde ve Ayarlar'da görünüyor, son değişiklikler Ayarlar'da listeleniyor. |
| 2 | 10 Ekim 2026 | Alt menü ekranın en altına sabitlendi; iPhone'da altta kalan boşluk giderildi. |
| 1 | 10 Ekim 2026 | İlk sürüm: 9 bulmaca, Kolay/Orta/Zor seviyeler, Google ile giriş, ana ekrana eklenebilir uygulama. |
