
# Full Adder Simülatörü

## 1. Öğrenci Bilgileri
-Ad Soyad: Ahmed Tarık Arslan
-Öğrenci Numarası: 25360859020
-Üniversite: Bursa Teknik Üniversitesi
-Bölüm: Bilgisayar Mühendisliği
-Ders: BLM101

## 2. Proje Konusu
Sayısal Mantık ve Aritmetik Devreler
(Full Adder Simülatörü)
Bu projenin amacı iki adet 4-bitlik sayıyı iki adet half adder(yarım toplayıcı) 
fonksiyonundan oluşan bir full adder(tam toplayıcı) simülatörü ile toplayan kodu 
geliştirmektir.

## 3. Proje Hakkında
Proje Python programlama dili ile geliştirilmiştir.Kullanıcıdan alınan iki 4-bitlik
ikili sayıyı mantık kapıları ile toplar ve sonucu ekrana yazdırır.Projede AND,OR,OXR
mantık kapıları ile bu kapılardan oluşan half adder ve full adder simülatörü kullanılmıştır.

## 4. Kullanılan Teknolojiler
-Python
 1.input() ve print() : Kullanıcıdan veri almak için ve sonucu görmek için kullanıldı.
 2.AND,XOR ve OR : Mantık kapıları toplama işlemini yapmak ve girilen sayılar yanlış mı kontrol 
 etmek için kullanıldı.
 3.if() :Girilen sayıların doğruluğunu kontrol etmek için kullanıldı.
-GitHub : Proje dosyalarının ve dokümantasyonun tutulduğu platform.

## 5. Kurulum ve Çalıştırma
1.Programı Çalıştırmak için bilgisayarda Python kurulu olmalıdır.(Version:2026.10.1)
2.Proje dosyalarından kodları kopyala-yapıştır yaparak ya da direk github üzerinden indirerek
kodları almak.
3.Terminal üzerinden şu kod çalıştırılır:(eğer klasör indirildiyse)python/src/Okul-Projesi.py
                                         (eğer kod kopyalandıysa)python üzerinden direk çalıştırabilirsiniz.
4.Kod kullanıcıdan iki sayı ister ve bu sayılar girilince kontrol eder eğer sayılar uygunsa toplama işlemini
yapar ama eğer değilse uyarı mesajı gönderir ve programı yeniden başlatma ister.

## 6. Algoritmanın Çalışma Mantığı
1.Kod kullanıcıdan iki 4-bitlik ikilik sayı ister.
2.Kod sayılar istenilen şekilde mi kontrol eder.(eğer değilse baştan 
başlatma istenir)
3.Sayıların bitleri sağdan sola doğru sırayla işlenir.
4.Her basamakta full adder ile toplama işlemi yapılır ve sonuç ile elde biti hesaplanır.
5.Tüm bitler işlendiğinde sonuç ekrana yazılır(eğer varsa nihai bit ile birlikte)

## 7. Proje Dosyaları
- src/: Python kaynak kodları
- sunum.pdf: Proje sunumu
- README.md : proje dokümantasyonu,öğrenci bilgileri
