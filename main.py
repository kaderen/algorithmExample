# 1. SORUNUN CEVABI

def tekSayilar():
    result = 0
    for i in range(1, 100, 2):
        result = result + i
    return result


def ciftSayilar():
    result = 0
    for i in range(0, 100, 2):
        result = result + i
    return result


print("0 dan 100'e kadar olan tek sayıların toplamı : ", tekSayilar())
print("0 dan 100'e kadar olan çift sayıların toplamı : ", ciftSayilar())

# 2. SORUNUN CEVABI

sayi = input("Ters çevirilecek sayıyı giriniz : ")
terssayi = sayi[::-1]
print(terssayi)

# 3.SORUNUN CEVABI


taban = int(input("Tabanı giriniz : "))
us = int(input("Üssü giriniz : "))
sonuc = 1
for i in range(us):
    sonuc = sonuc * taban
print("Üs alma işleminin sonucu : ", sonuc)


# 4. SORUNUN CEVABI

def fibonacci(sinir):
    i = 0
    result = 1
    while i < sinir:
        print(i, end=", ")
        n = result + i
        i = result
        result = n


print(fibonacci(100), end="")


# 5. SORUNUN CEVABI

def fibonacciDizili(sinir):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    for i in range(sinir - 2):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    return fibonacci


print()
print(fibonacciDizili(12))

# 6. SORUNUN CEVABI

ogrenciList = []
vizeList = []
finalList = []
agno=[]
for i in range(5):
    print(i+1,". öğrencinin ismini giriniz : ",end="")
    isim = input()
    print(i + 1, ". öğrencinin vize giriniz : ", end="")
    vize = int(input())
    print(i + 1, ". öğrencinin final giriniz : ", end="")
    final = int(input())
    ogrenciList.append(isim)
    vizeList.append(vize)
    finalList.append(final)
    notOrt=vize*0.4 + final*0.6
    agno.append(notOrt)
toplamAgno=sum(agno)
can=toplamAgno/5
for i in range(5):
    if agno[i] <= can:
        print(ogrenciList[i] , " KALDI")
    else:
        print(ogrenciList[i]," GEÇTİ")

#7. SORUNUN CEVABI

for i in range(1,101,2):
    print(i,"-----",i+1)



#8. SORUNUN CEVABI
liste=[]
for i in range(5):
    sayi=int(input("Sayı giriniz : "))
    liste.append(sayi)
print(sorted(liste))


#9. SORUNUN CEVABI
def faktoriyel(sayi):
    result=1
    for i in range(1,sayi+1):
        result*=i
    return result

faktoriyelSayi = int(input("Faktoriyel almak istediğiniz sayıyı giriniz : "))
print(faktoriyel(faktoriyelSayi))


#10. SORUNUN CEVABI

def carpma(sayi1,sayi2):
    result2 = 0
    for i in range(sayi2):
        result2+=sayi1
    return result2
sayi1=int(input("Sayı 1'i giriniz : "))
sayi2 = int(input("Sayı 2'yi giriniz : "))
print(carpma(sayi1,sayi2))