import csv

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv","w",newline="")as f:
    w = csv.writer(f)
    w.writerow(["nom", "narx", "soni"])
    w.writerows(mahsulotlar)