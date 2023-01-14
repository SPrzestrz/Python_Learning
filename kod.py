# Importujemy biblioteke random
import random as r
# Tworzymy pętlę while co oznacza że będzie się powtarzać aż wartość quit nie będzie True
quit = False
while(quit!=True):
    # Losujemy liczbe z przedziału od 0 do 10 dzięki funkcji randint z biblioteki
    traf = r.randint(0,100)
    print("Podaj liczbe:")
    # Wprowadzamy własną liczbę 
    liczba = input()
    czyliczba = True
    liczby = ["0","1","2","3","4","5","6","7","8","9"]
    for i in liczba:
        if(i not in liczby):
            czyliczba=False
    if(czyliczba==False):
        print("Podaj liczbe nie litere")
    else:
        if(int(liczba)!=traf):
            print(f"traf = {traf}, liczba = {liczba}")
            print("Nie trafiles")
        else:
            print(f"traf = {traf}, liczba = {liczba}")
            print("Brawo trafiles")
            break

    