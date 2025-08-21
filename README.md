# 🛡️ XSS Scanner (Python)  
**Etkili bir XSS zafiyeti tarayıcısı**

---

## 📌 Hakkında

Bu proje, hedef web sitelerinde **Reflected**, **Stored** ve basit düzeyde **DOM-based XSS (Cross Site Scripting)** açıklarını tespit etmek amacıyla geliştirilmiş bir Python tabanlı tarayıcıdır.

Aracın temel işlevleri:

- URL üzerindeki GET parametrelerini test etme  
- HTML formları üzerinden POST/GET bazlı XSS taraması  
- Sayfa kaynaklarında basit DOM XSS belirtilerini kontrol etme  
- Otomatik rapor üretimi (JSON ve HTML)

---

## ⚠️ Yasal Uyarı

> 🚨 **Bu araç yalnızca yetkilendirilmiş testler için kullanılmalıdır.**  
Yetkisiz sistemlerde kullanım _suç teşkil eder_ ve etik dışıdır.  
Aracı yalnızca **izinli test ortamlarında** veya eğitim amaçlı lab sistemlerinde çalıştırınız.

---

## 🧰 Gereksinimler

- Python 3.7+  
- `requests`  
- `beautifulsoup4`

Kurmak için:

```bash
pip install -r requirements.txt
requirements.txt yoksa:


pip install requests beautifulsoup4
🚀 Kullanım

python3 test.py
Program çalıştırıldığında terminalde sana aşağıdaki gibi bir ekran sunulur:



====================================
     🚨 XSS Scanner Başlatıldı 🚨
====================================

Kullanım:
- Hedef URL'yi tam olarak girin (örn: https://example.com)
- Tarama tamamlandığında raporlar 'report.json' ve 'report.html' olarak kaydedilecek.
📄 Raporlar
Tarama sonucu aşağıdaki dosyalar otomatik oluşturulur:

report.json → Yapılandırılmış makine-okunabilir çıktı

report.html → Renkli, kolay okunabilir insan dostu rapor

🔍 Örnek Test Siteleri
Projeyi test etmek için OWASP ve PortSwigger gibi güvenli ve yetkilendirilmiş lab siteleri kullanılmalıdır:

https://xss-game.appspot.com/

https://portswigger.net/web-security/cross-site-scripting

https://owasp.org/www-project-webgoat/

https://dvwa.co.uk/

🧪 Özellikler
✅ GET parametre testleri

✅ Form tabanlı (POST & GET) XSS denemeleri

✅ DOM tabanlı XSS belirtilerini tanıma

✅ Tekrarlayan sonuçları filtreleme

✅ Esnek payload yönetimi (dış dosyadan yüklenebilir)

✅ Şık ve sade terminal arayüzü



📜 Lisans
MIT License
