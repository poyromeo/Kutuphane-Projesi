import sqlite3
import time

class Kitap():

    def __init__(self,isim,yazar,yayınevi,tür,baskı):

        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı

    def __str__(self):

        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)


class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitapları_goster(self):

        sorgu =  "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor.....")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])

            print(kitap)
    def kitap_ekle(self,isim,yazar,yayinevi,tur,baski):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(isim,yazar,yayinevi,tur,baski))

        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def baskı_yükselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            baskı = kitaplar[0][4]

            baskı += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baskı,isim))

            self.baglanti.commit()


print("""
***********************************

Sarkı kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap sorgula

3. Kitap ekle

4. Kitap sil

5. Baskı yükselt

Çıkmak için 'q' ya basın.
************************************
""")

kutuphane = Kütüphane()


while True:
    islem = input("bir işlem giriniz :")

    if islem == 'q':
        print("sistem kapatıldı...")
        break

    elif islem == '1':
        kutuphane.kitapları_goster()

    elif islem == '2':
        kitap_ismi = input("Kitap isimin giriniz :")
        time.sleep(0.5)
        print("kitap sorgulanıyor...")
        print("******************************************")
        time.sleep(2)
        kutuphane.kitap_sorgula(kitap_ismi)



    elif islem == '3':

        isim = input("kitap ismi :")
        yazar = input("yazar ismi :")
        yayinevi = input("yayınevi giriniz :")
        tur = input("Kitabın Türünü giriniz :")
        baski = float(input("Baskı :"))


        kutuphane.kitap_ekle(isim,yazar,yayinevi,tur,baski)
        print("kitap ekleniyokr...")
        time.sleep(2)
        print("kitap eklendi....")

    elif islem == '4':
        kitap_ismi = input("Kitap ismini giriniz :")
        time.sleep(1)
        cevap = input("Emin misiniz ? (E/H)")
        if cevap == 'E':
            print("sarkı siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(kitap_ismi)
            print("şarkı silindi...")

    elif islem == '5':
        kitap_ismi = input("Baskı yükseltilcek kitap ismini giriniz : ")
        kutuphane.baskı_yükselt(kitap_ismi)
        print("baskı +1 yükseltiliyor...")
        time.sleep(1)
        print("Baskı yülseltildi.")

































