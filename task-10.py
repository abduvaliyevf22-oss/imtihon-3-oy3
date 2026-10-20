from matplotlib import pyplot
kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

pyplot.plot(kunlar,daromad,label="daromad")
pyplot.title("7 kun uchun chiziqli grafik yaratiladi.")
pyplot.ylabel("daromadlar")
pyplot.xlabel("hafta kunlari")
pyplot.grid(True)
pyplot.legend()
pyplot.savefig("daromad.png")
