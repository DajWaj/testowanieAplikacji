import random

wyniki = []
wybor = ''
suma2 = 0
zmienna = []

while True:
    liczba_kostek = int(input("Ile kostek chcesz rzucić? (3 - 10)\n"))
    if liczba_kostek >= 3 and liczba_kostek <= 10:

        for x in range(0, liczba_kostek):
            wyniki.append(random.randint(1, 6))

        i=0
        for wynik in wyniki:
            i=i+1
            print("Kostka "+str(i)+": "+str(wynik))

        for i in wyniki:
            l = 0 # ile razy
            suma = 0 # suma tej samej liczby
            bomba = 0 # czy liczba sie powtarza
            for g in zmienna:
                if i == g:
                    bomba+=1
            if bomba>1: continue
            for j in wyniki:
                if i == j:
                    l = l + 1
                    suma += j
                    zmienna.append(i)
            if l>1:
                suma2 += suma

        print("Liczba uzyskanych punktów: "+str(suma2)+"\n")
        wybor = input("Jeszcze raz? (t/n)\n")
    if wybor == 'n': break



