import random

# Uzytkownik podaje ile kostek chce rzucic, weryfikacja poprawnosci
while True:
    liczba_kostek = input("Ile kostek chcesz rzucić? (3-10): ")
    if liczba_kostek.isnumeric():
        if float(liczba_kostek) == int(liczba_kostek) and int(liczba_kostek) >= 3 and int(liczba_kostek) <= 10:
            liczba_kostek = int(liczba_kostek)
            break

while True:

    # Losowanie kostek uzytkownika
    wylosowane = []
    for i in range(0, liczba_kostek):
        wylosowane.append(random.randint(1, 6))
        print("Kostka " + str(i+1) + ": " + str(wylosowane[i]))

    # Liczenie punktów i wypisywanie wyniku
    wynik = 0
    for x in wylosowane:
        pom = 0
        for y in wylosowane:
            if x == y: pom += 1
        if pom > 1: wynik += x
    print("Liczba uzyskanych punktów: " + str(wynik))

    # Uzytkownik podaje czy chce jeszcze grac czy nie, weryfikacja poprawnosci
    while True:
        wybor = input("Jeszcze raz? (t/n): ")
        if wybor == 't' or wybor == 'n': break

    if wybor == 'n': break