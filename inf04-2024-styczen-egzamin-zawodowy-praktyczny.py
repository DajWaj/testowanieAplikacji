wagi = str(1379137913)

def sprawdzaniePlci(pesel):
    if int(pesel[9])%2 == 0: return 'K'
    else: return 'M'

def sprawdzanieSumyKontrolnej(pesel):
    S = 0
    for i in range(10):
        S += int(pesel[i])*int(wagi[i])
    
    M = S%10
    if M == 0: R = 0
    else: R = 10-M
    if R == int(pesel[10]): return True
    else: return False

while True:
    bledy = 0
    pesel = input("Podaj numer pesel: ")
    if len(pesel) != 11: bledy+=1
    if pesel.isnumeric() == False: bledy+=1
    if bledy == 0: break

print(sprawdzaniePlci(pesel))
print(sprawdzanieSumyKontrolnej(pesel))