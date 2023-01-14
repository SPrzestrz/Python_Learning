

# Szymon 
# Napisz program który pobierze imię i liczbę i wypisze to połączone w jednej linijce 
imie = input("podaj imie: ")
print(f"Czesc {imie} ile masz lat")
liczba = input("podaj wiek: ")
print(f"Czesc {imie} fajnie że masz {liczba} lat")
if(int(liczba)<20):
    print("Siemanko")
else: 
    print("Witam")
praca = input("gdzie pracujesz: ")
if(praca.lower()=="zus"):
    print(f"słabo ze pracujesz w {praca} to chyba malo zarabiasz")
else:
    print(f"Fajnie ze pracujesz w {praca} mam nadzieje że dużo zarabiasz")


