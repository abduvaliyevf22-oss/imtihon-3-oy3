

import json


with open("products.json", "r", ) as f:
    ozgaruvchi = json.load(f)

maxsulot = input("Mahsulot nomi: ").lower()
miqdor = int(input("Yangi miqdor: "))

topildi = False

for i in range(len(ozgaruvchi)):
    if maxsulot == ozgaruvchi[i]["nom"].lower():
        ozgaruvchi[i]["miqdor"] = miqdor
        topildi = True
        break

if topildi:
  
    with open("products.json", "w") as f:
        json.dump(ozgaruvchi, f)
    print("yangilandi")
else:
    print("Mahsulot topilmadi")