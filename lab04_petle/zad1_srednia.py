# Lab 04 – Zadanie 1 (★): Średnia ocen
#
# Program wczytuje oceny (float), każdą w osobnej linii, aż użytkownik
# wciśnie Enter w pustej linii. Potem wypisuje średnią z 2 miejscami, np.:
#     Średnia ocen: 4.00
# Jeśli nie podano żadnej oceny, wypisz: Brak ocen
#
# Wskazówki:
#   - pętla while True + break, gdy linia jest pusta
#   - licz sumę i liczbę ocen w dwóch zmiennych

# TODO: Twój kod poniżej

suma = 0.0
liczba = 0

while True:
    linia = input()
    if linia == "":
        break
    suma += float(linia)
    liczba += 1

if liczba == 0:
    print("Brak ocen")
else:
    print(f"Średnia ocen: {suma / liczba:.2f}")