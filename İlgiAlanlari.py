def ilgi_alani_gir(kisi_ad):
    print(f"{kisi_ad} adli kisiye ait ilgi alanlarini girin:(Bitirmek için q yu tuşlayin)")
    alanlar=set()
    while True:
        girdi=input("ilgi alani:")
        if girdi.lower()=="q" :
            break
        else:
            alanlar.add(girdi.lower)
    return alanlar

kisi1_ile_ilgili_bilgiler=ilgi_alani_gir("Ali")
kisi2_ile_ilgili_bilgiler=ilgi_alani_gir("Ahmet")

ortak=kisi1_ile_ilgili_bilgiler & kisi2_ile_ilgili_bilgiler
sadece_ali=kisi1_ile_ilgili_bilgiler - kisi2_ile_ilgili_bilgiler
sadece_ahmet=kisi2_ile_ilgili_bilgiler - kisi1_ile_ilgili_bilgiler
birlesim=kisi1_ile_ilgili_bilgiler | kisi2_ile_ilgili_bilgiler

print("\n--- SONUÇLAR ---")
print("Ortak ilgi alanları:", ortak if ortak else "Yok")
print(" Ali'ye özel ilgi alanları:", sadece_ali if sadece_ali else "Yok")
print(" Ayşe'ye özel ilgi alanları:", sadece_ahmet if sadece_ahmet else "Yok")
print(" Tüm ilgi alanları:", birlesim)

