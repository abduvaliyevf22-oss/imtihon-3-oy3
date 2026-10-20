
def koeffitsiyentlar(a):
    def qiymat(b):
        return a*b
    return qiymat

koeffitsiyent = 7
qiymat = 4

amal = koeffitsiyentlar(koeffitsiyent)
natija = amal(qiymat)

print(f"Natija:{natija}")
