
sonlar = [12, 7, 5, 18, 9, 4]
def tahlil_qil(sonlar):
    juft_sonlar = 0
    toq_sonlat = 0
    eng_katta=sonlar[0]

    for i in sonlar:
        if i%2==0:
             juft_sonlar+=i
        else:
            toq_sonlat+=i
        if i > eng_katta:
            eng_katta = i
         
    print(f"Juft sonlar yig'indisi: {juft_sonlar}")
    print(f"Toq sonlar yig'indisi: {toq_sonlat}")
    print(f"Eng katta son: {eng_katta}")

tahlil_qil(sonlar)

