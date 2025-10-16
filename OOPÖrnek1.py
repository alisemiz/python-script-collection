class Student:
    def __init__(self, isim, yas, notOrtalamasi):
        self.isim = isim
        self.yas = yas
        self.notOrtalamasi = notOrtalamasi

    def bilgileriGoster(self):
        return f"İsim: {self.isim}  Yaş: {self.yas}  Not: {self.notOrtalamasi}"

    def durum(self):
        # Eğer 4 üzerinden not sistemi ise:
        if self.notOrtalamasi >= 2.0:
            print(f"{self.isim} Geçti")
        else:
            print(f"{self.isim} Kaldı")


# Öğrenciler
student1 = Student("Ali", 21, 3.21)
student2 = Student("Mehmet", 22, 1.5)

# Bilgi ve durum yazdırma
print(student1.bilgileriGoster())
student1.durum()

print(student2.bilgileriGoster())
student2.durum()
