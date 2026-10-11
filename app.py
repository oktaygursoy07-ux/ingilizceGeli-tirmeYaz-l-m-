kelimeler = { "apple" :"elma" , 
             "book":"kitap", "house": "ev",
             "computer":"bilgisayar",
             "water":"su",
             "cat":"kedi"}

puan =0 
dogru_sayisi = 0 
print("İNGİLİZCE KELİME OYUNU\n")
print("her doğru cevap 0 puan")

for ingilizce, turkce in kelimeler.items():
    cevap = input(
        ingilizce + " kelimesinin türkçe karsiliginiz"
    ).strip().lower()

    if cevap == turkce:
        puan += 10 
        print("Tebrikler kelimeyi dogru bildiniz!")
        dogru_sayisi += 1
    elif cevap != turkce:
        if puan >5:
            puan -= 5
        else:
            puan = 0
        print("yanlış! kelimelerin karsiligini yanlis yazdiniz!")        
print("kazandiginiz toplam puan:",puan)     

if puan >= 60 :
    print("tam puan aldın! sonraki seviyeye geçmeye hak kazandiniz!")
elif puan <= 40:
    print("sonraki seviyeye geçemezsin! daha fazla kelime pratigi yapmalisin!")  
else: 
    print("ingilizce seviyen: orta -- sonraki seviye için daha fazla kelime bilmelisin!")      
