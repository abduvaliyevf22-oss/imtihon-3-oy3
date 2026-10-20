mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}
Mahsulot_nomi = input("mahsulot nomi:")
Yangi_narx = int(input("yangi narx:"))

if Mahsulot_nomi in mahsulotlar:
    mahsulotlar[Mahsulot_nomi]=Yangi_narx
    print("narx yangilandi")
    print(mahsulotlar)
else:
    print("xatolik")