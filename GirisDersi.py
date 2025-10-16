# Kullanıcı bilgileri (sabit)
kayitli_kullanici_adi = "admin"
kayitli_sifre = "12345"

# Giriş sayacı
deneme_hakki = 3

while deneme_hakki > 0:
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")

    if kullanici_adi == kayitli_kullanici_adi and sifre == kayitli_sifre:
        print("✅ Giriş başarılı! Hoş geldin,", kullanici_adi)
        break
    else:
        deneme_hakki -= 1
        print("❌ Hatalı giriş. Kalan deneme hakkı:", deneme_hakki)

if deneme_hakki == 0:
    print("🚫 Hesabınız bloke oldu. Lütfen daha sonra tekrar deneyin.")
