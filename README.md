# Flask REST API ve Debian Paketi Projesi

Bu proje, Flask tabanlı bir REST API uygulaması geliştirme, bu uygulamayı bir **systemd servisi** olarak çalıştırma ve hem uygulamayı hem de servisi bir Debian paketi olarak dağıtma işlemlerini kapsamaktadır.

---

## Proje Yapısı
Proje dosyalarının daha düzenli bir şekilde organize edilmesi için aşağıdaki klasör yapısı oluşturulmuştur:

```
YMG1/
│
├── app/
│   ├── api.py                 # Flask uygulaması
│   ├── requirements.txt       # Uygulamanın bağımlılıklarını içeren dosya
│
├── service/
│   ├── myapp.service          # systemd servis dosyası
│
├── package/
│   ├── build.sh               # Debian paketi oluşturmak için betik
│
├── README.md                  # Proje açıklamaları ve kurulum talimatları
```

---

## API Özellikleri
Proje, aşağıdaki endpoint'leri sunmaktadır:

### 1. GET `/add`
**Açıklama**: İki sayıyı toplar ve sonucu döner.  
**Parametreler**:
- `num1`: İlk sayı (zorunlu, tam sayı)
- `num2`: İkinci sayı (zorunlu, tam sayı)

**Örnek Kullanım**:
```bash
curl "http://127.0.0.1:2700/add?num1=5&num2=10"
```

**Beklenen Yanıt**:
```json
{
  "result": 15
}
```

---

### 2. POST `/multiply`
**Açıklama**: JSON formatında iki sayıyı alır, çarpar ve sonucu döner.  
**Gönderilen JSON**:
```json
{
  "num1": 3,
  "num2": 4
}
```

**Örnek Kullanım**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"num1": 3, "num2": 4}' http://127.0.0.1:2700/multiply
```

**Beklenen Yanıt**:
```json
{
  "result": 12
}
```

---

## Kurulum Talimatları

### 1. Flask Uygulamasının Çalıştırılması
1. **Gerekli Bağımlılıkları Yükleyin**:
   ```bash
   pip install -r app/requirements.txt
   ```
2. **Uygulamayı Başlatın**:
   ```bash
   python3 app/api.py
   ```

3. **API'nin Çalıştığını Doğrulayın**:
   - Tarayıcınızdan veya `curl` komutuyla `http://127.0.0.1:2700` adresine ulaşabilirsiniz.

---

### 2. Servis Kurulumu
Flask uygulamasını bir **systemd servisi** olarak çalıştırmak için:

1. **Servis Dosyasını Kopyalayın**:
   ```bash
   sudo cp service/myapp.service /etc/systemd/system/
   ```

2. **Servisi Etkinleştirin ve Başlatın**:
   ```bash
   sudo systemctl enable myapp
   sudo systemctl start myapp
   ```

3. **Servisin Durumunu Kontrol Edin**:
   ```bash
   sudo systemctl status myapp
   ```

---

### 3. Debian Paketi Oluşturma
Uygulamayı ve servisi bir Debian paketi olarak dağıtmak için:

1. **Debian Paketi Betiğini Çalıştırın**:
   ```bash
   cd package
   bash build.sh
   ```

2. **Oluşan Paketi Kurun**:
   ```bash
   sudo dpkg -i myapp_1.0_amd64.deb
   ```

3. **Paketi Kaldırma**:
   ```bash
   sudo apt remove myapp
   ```

---

## Geliştirici Notları
- Flask uygulaması, **2700** numaralı port üzerinden çalışmaktadır (memleket plaka kodu gereksinimine uygun olarak).
- Servis, `systemctl` ile yönetilebilir ve otomatik olarak başlatılabilir.
- `fpm` aracı kullanılarak Debian paketi oluşturulmuştur.

---

## Proje Gereksinimleri
Bu proje, aşağıdaki teknik gereksinimleri karşılamaktadır:
1. Flask REST API oluşturulması.
2. GET ve POST endpoint'leri eklenmesi.
3. Varsayılan port yerine memleket plaka numarasına göre yayın yapılması.
4. Systemd servisi oluşturulması.
5. Uygulama ve servisin Debian paketi haline getirilmesi.

---

## Test Süreci
- **API Testleri**: `curl` ile GET ve POST endpoint'leri test edilmiştir.
- **Servis Testleri**: Servis başarıyla başlatılmış, durdurulmuş ve yeniden başlatılmıştır.
- **Debian Paket Testleri**: Paket kurulumu ve kaldırma işlemleri başarıyla gerçekleştirilmiştir.

---

## Lisans
Bu proje açık kaynak olarak sunulmuştur. Herhangi bir amaçla kullanılabilir.


