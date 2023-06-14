#Zadanie 1
import random

def rzut_koscia():
    return random.randint(1, 6)
print("Masz trzy próby na uzyskanie jak najwyższego wyniku.")

wynik = 0

for _ in range(3):
    input("Naciśnij Enter, aby rzucić kością...")
    rzut = rzut_koscia()
    print("Wynik rzutu: ", rzut)
    wynik += rzut

print("Koniec gry!")
print("Twój łączny wynik: ", wynik)

#Zadanie 2
haslo = "haslo"

wprowadzone_haslo = input("Podaj hasło: ")

if wprowadzone_haslo == haslo:
    print("Poprawne hasło.")
else:
    print("Nieprawidłowe hasło")

#Zadanie 3
class Osoba:
    def __init__(self, nazwa_uzytkownika, haslo, poziom_uprawnien):
        self.nazwa_uzytkownika = nazwa_uzytkownika
        self.haslo = haslo
        self.poziom_uprawnien = poziom_uprawnien


def logowanie(nazwa_uzytkownika, haslo):

    osoby = [
        Osoba("admin", "admin123", 3),
        Osoba("uzytkownik1", "haslo123", 1),
        Osoba("uzytkownik2", "haslo456", 2),
        Osoba("uzytkownik3", "haslo789", 1)
    ]

    for osoba in osoby:
        if osoba.nazwa_uzytkownika == nazwa_uzytkownika and osoba.haslo == haslo:
            print("Zalogowano pomyślnie.")
            if osoba.poziom_uprawnien == 1:
                print("Masz podstawowe uprawnienia.")
            elif osoba.poziom_uprawnien == 2:
                print("Masz zaawansowane uprawnienia.")
            elif osoba.poziom_uprawnien == 3:
                print("Jesteś administratorem klubu.")
            return

    print("Nieprawidłowe dane logowania")


nazwa_uzytkownika = input("Podaj nazwę użytkownika: ")
haslo = input("Podaj hasło: ")

logowanie(nazwa_uzytkownika, haslo)

#Zadanie 4
import random

przepowiednie = [
    "Twoje marzenia się spełnią w najbliższym czasie.",
    "Przed Tobą ważna decyzja, postępuj rozważnie.",
    "Poczujesz się spełniony/a w miłości.",
    "Twój talent zostanie dostrzeżony przez innych."
]

wylosowana_przepowiednia = random.choice(przepowiednie)
print("Przepowiednia:")
print(wylosowana_przepowiednia)

#Zadanie 5
import random

def rzut_moneta():
    wynik = random.randint(0, 1)
    if wynik == 0:
        return "orzeł"
    else:
        return "reszka"

def symulacja_rzutu_moneta(liczbaRzutow):
    orly = 0
    reszki = 0

    for _ in range(liczbaRzutow):
        wynik = rzut_moneta()
        if wynik == "orzeł":
            orly += 1
        else:
            reszki += 1

    print("Liczba orłów:", orly)
    print("Liczba reszek:", reszki)

liczbaRzutow = 100
symulacja_rzutu_moneta(liczbaRzutow)

#Zadanie 6
class Telewizor:
    def __init__(self):
        self.kanal = 1
        self.glosnosc = 50

    def zmien_kanal(self, nowy_kanal):
        self.kanal = nowy_kanal
        print("Zmieniono kanał na", self.kanal)

    def zwieksz_glosnosc(self):
        if self.glosnosc < 100:
            self.glosnosc += 1
        print("Głośność:", self.glosnosc)

    def zmniejsz_glosnosc(self):
        if self.glosnosc > 0:
            self.glosnosc -= 1
        print("Głośność:", self.glosnosc)


telewizor = Telewizor()

while True:
    print("Telewizor")
    print("1. Zmień kanał")
    print("2. Zwiększ głośność")
    print("3. Zmniejsz głośność")
    print("0. Wyłącz telewizor")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nowy_kanal = input("Podaj numer kanału: ")
        telewizor.zmien_kanal(nowy_kanal)
    elif wybor == "2":
        telewizor.zwieksz_glosnosc()
    elif wybor == "3":
        telewizor.zmniejsz_glosnosc()
    elif wybor == "0":
        print("Telewizor wyłączony.")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")



