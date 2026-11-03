# Lab 04 – Zadanie 3 (★): Suma i liczba cyfr
#
# Program wczytuje nieujemną liczbę całkowitą i wypisuje DOKŁADNIE:
#     Suma cyfr: 15
#     Liczba cyfr: 5
# (dla 12345).
#
# Rozwiąż to ARYTMETYCZNIE pętlą while, bez zamiany na tekst:
#   - n % 10 to ostatnia cyfra,
#   - n // 10 „odcina” ostatnią cyfrę.
# Uwaga: liczba 0 ma jedną cyfrę.

# TODO: Twój kod poniżej

n = int(input())

suma = 0
liczba = 0

if n == 0:
    liczba = 1
else:
    while n > 0:
        suma += n % 10
        liczba += 1
        n //= 10

print(f"Suma cyfr: {suma}")
print(f"Liczba cyfr: {liczba}")