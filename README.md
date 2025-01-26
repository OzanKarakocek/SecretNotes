# Secret Notes Uygulaması

Secret Notes, önemli notlarınızı şifreli bir şekilde saklamanızı ve gerektiğinde güvenle görüntülemenizi sağlayan bir uygulamadır. Şifrelenmiş notlarınızı yalnızca belirttiğiniz master key ile çözebilirsiniz. Master key'inizi unutmayın! Aksi takdirde notlarınızın şifrelerini çözemezsiniz.

## Özellikler

- Başlık, Gizli Not ve Master Key giriş alanları.

- AES şifreleme yöntemi ile notlarınızı şifreler.

- Şifrelenmiş notları metin dosyasına kaydeder.

- Şifre çözme işlemi ile notlarınıza erişim sağlar.

- Kullanıcı dostu arayüz.

### Kullanım

**Not Kaydetme:**

Başlık, gizli not ve bir master key girin.

"Save & Encrypt" butonuna tıklayarak notunuzu şifreleyin ve bilgisayarınıza kaydedin.

**Not Çözme:**

Kaydedilen notun başlığını ve master key'i girin.

"Decrypt" butonuna tıklayarak şifrelenmiş notunuzu çözün.

### Gereksinimler

- Python 3.x

- Gerekli kütüphaneler: tkinter, Pillow, cryptography

### Kurulum

**Gerekli Paketleri Yükleyin:**

`pip install -r requirements.txt`

**Uygulamayı Çalıştırın:**

`python main.py`

