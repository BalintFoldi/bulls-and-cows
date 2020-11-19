import random

szam = []
probalkozas = 0

def szam_letrehozas():
    for i in range(4):
        x = random.randrange(0, 9)
        szam.append(x)
    for i in range(len(szam)):
        for j in range(i + 1, len(szam)):
            if szam[i] == szam[j]:
                szam.clear()
                szam_letrehozas()

def jatek():
    global probalkozas
    probalkozas += 1
    cows = 0
    bulls = 0

    valasz = input("Kérlek adj meg egy 4 jegyű számot: ")
    tipp = []
    for i in range(4):
        tipp.append(int(valasz[i]))
    for a in range(4):
        for b in range(4):
            if tipp[a] == szam[b]:
                cows += 1
    for x in range(4):
        if tipp[x] == szam[x]:
            bulls += 1
            cows -= 1
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    if bulls == 4:
        print("Nyertél", probalkozas, "próbálkozásból")
    elif bulls != 4:
        jatek()

# fő program
print("Ez a Bulls and Cows játék, ki kell találnod, hogy a gép milyen 4 jegyű számmra gondolt")
szam_letrehozas()
jatek()
