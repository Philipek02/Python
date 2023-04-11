# zad 1
print("zad 1")
print("Filip Olek Piotr Krystian Marcin")
# zad 2
print("zad 2")
print("Filip \nOlek \nPiotr \nKrystian \nMarcin")
# zad 3
print("zad 3")
a = 3
b = 4
for j in range(a):
    for i in range(b):
        print("*", end = " ")
    print()

# zad 4
print("zad 4")
print("Ceny przed: 3.69, 4.5, 3.6, 4.0, 3.99, 3.59\n"
      "Ceny po: 4.5, 5.5, 4.69, 4.99, 4.00")
cenyPrzed = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
cenyPo = [4.5, 5.5, 4.69, 4.99, 4.00]
wszystkieCeny = cenyPo + cenyPrzed
maxPo = 0
maxPrzed = 0
print(max(cenyPo))
print(min(wszystkieCeny))
print(sum(cenyPrzed)/len(cenyPrzed))
print(sum(cenyPo)/len(cenyPo))
# zad 5
print("zad 5")
i1 = "John"
i2 = "Pete"
i3 = "Bob"
i4 = "Patrick"
i5 = "Salah"
imionaBohaterow = {i1 : len(i1), i2 : len(i2),i3 : len(i3),i4 : len(i4),i5 : len(i5) }
print(imionaBohaterow)
# zad 6
print("zad 6")
n = int(input("podaj liczbe: "))
print("wartosc bezwgl: " + str(abs(n)))
# zad 7
print("zad 7")
m = int(input("podaj dzielnik: "))
for i in range(20, 81):
    if i % m == 0:
        print(i, end = " ")
# zad 8
print("zad 8")
m = int(input("podaj dzielnik: "))
x = int(input("podaj dolna granice zakresu: "))
y = int(input("podaj gorna granice zakresu: "))

for i in range(x, y):
    if i % m == 0:
        print(i, end = " ")

# zad 9
print("zad 9")
a1 = int(input("podaj pierwsza liczbe: "))
b1 = int(input("podaj druga liczbe: "))
c1 = int(input("podaj trzecia liczbe: "))
if a1 > 0 and b1 > 0 and c1 > 0:
    if a1 + b1 == c1:
        print("to jest trojka pitagorejska:)")
    else:
        print("to nie jest trojka pitagorejska:(")
else:
    print("wszystkie liczby musza byc > 0")

# zad 10
print("zad 10")
imie1 = input("Podaj pierwsze imię: ")
imie2 = input("Podaj drugie imię: ")
if imie1 == imie2:
    print("Podane imiona są identyczne.")
else:
    print("Podane imiona są różne.")
# zad 11
print("zad 11")
i = 1
suma = 0
while i < 100:
    suma = suma + i
    i = i+2

print("suma: " + str(suma))