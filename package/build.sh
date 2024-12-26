#!/bin/bash

# Paketleme için gerekli klasörleri oluştur
mkdir -p myapp/opt/myapp
mkdir -p myapp/etc/systemd/system

# Flask uygulama dosyalarını kopyala
cp ../app/* myapp/opt/myapp/

# Servis dosyasını kopyala
cp ../service/myapp.service myapp/etc/systemd/system/

# Debian paketi oluştur
fpm -s dir -t deb -n myapp -v 1.0 --deb-systemd myapp/etc/systemd/system/myapp.service -C myapp .

# Geçici dosyaları temizle
rm -rf myapp

echo "Debian paketi oluşturuldu: myapp_1.0_amd64.deb"
