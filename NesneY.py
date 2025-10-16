class araba:
    def __init__(self,model,renk,fiyat):
        self.model=model
        self.renk=renk
        self.fiyat=fiyat

    def show_info(self):
        print(f"{self.model} -  {self.renk} - {self.fiyat}")




araba1=araba(2024,"siyah",2000000)
araba1.show_info()




        