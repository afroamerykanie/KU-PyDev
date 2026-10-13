# Lab 02 – Zadanie 1 (★): Kalkulator konsolowy
#
# Program wczytuje dwie liczby (float) i wypisuje wynik WSZYSTKICH działań,
# każde w osobnej linii, np. dla 7 i 2:
#     7.0 + 2.0 = 9.0
#     7.0 - 2.0 = 5.0
#     7.0 * 2.0 = 14.0
#     7.0 / 2.0 = 3.5
#     7.0 // 2.0 = 3.0     (dzielenie całkowite)
#     7.0 % 2.0 = 1.0      (reszta z dzielenia)
#     7.0 ** 2.0 = 49.0    (potęgowanie)
#
# Załóż, że druga liczba nie jest zerem (obsługę zera dodasz w labie 03).

# TODO: Twój kod poniżej
liczba = float(input("Podaj liczbę: "))
liczba2 = float(input("Podaj drugą liczę: "))
dodawanie = liczba + liczba2
odejmowanie = liczba - liczba2
mnozenie = liczba * liczba2
dzielenie = liczba / liczba2
dzielenie_calkowite = liczba // liczba2
reszta_z_dzielenia = liczba % liczba2
potegowanie = liczba ** liczba2

print(f"{liczba} + {liczba2} = {dodawanie}")
print(f"{liczba} - {liczba2} = {odejmowanie}")
print(f"{liczba} * {liczba2} = {mnozenie}")
print(f"{liczba} / {liczba2} = {dzielenie}")
print(f"{liczba} // {liczba2} = {dzielenie_calkowite}")
print(f"{liczba} % {liczba2} = {reszta_z_dzielenia}")
print(f"{liczba} ** {liczba2} = {potegowanie}")