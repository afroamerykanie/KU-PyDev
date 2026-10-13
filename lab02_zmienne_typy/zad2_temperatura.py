# Lab 02 – Zadanie 2 (★): Konwerter temperatury
#
# 1. Wczytaj temperaturę w stopniach Celsjusza i wypisz ją w Fahrenheitach:
#        F = C * 9 / 5 + 32
# 2. Wczytaj temperaturę w stopniach Fahrenheita i wypisz ją w Celsjuszach:
#        C = (F - 32) * 5 / 9
#
# Przykład: 37 °C = 98.6 °F,  212 °F = 100.0 °C
# Wyniki zaokrąglij do 1 miejsca po przecinku: f"{x:.1f}"

# TODO: Twój kod poniżej
celsjusz = float(input("1. Podaj temperature w Celsjuszach: "))
fahrenheit = celsjusz * 9 / 5 + 32
print(f"{celsjusz:.1f} °C = {fahrenheit:.1f} °F")
fahrenheit = float(input("2. Podaj temperature w Fahrenheitach: "))
celsjusz = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit:.1f} °F = {celsjusz:.1f} °C")