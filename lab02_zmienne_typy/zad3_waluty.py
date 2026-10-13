# Lab 02 – Zadanie 3 (★): Przelicznik walut
#
# Program wczytuje kwotę w złotych i wypisuje jej równowartość w EUR i USD,
# zaokrągloną do 2 miejsc po przecinku, np. dla 425 zł:
#     425.00 PLN = 100.00 EUR
#     425.00 PLN = 111.84 USD
#
# Kursy są STAŁE (na potrzeby zadania – nie są to aktualne kursy NBP):

EUR_RATE = 4.25   # 1 EUR = 4.25 PLN
USD_RATE = 3.80   # 1 USD = 3.80 PLN

# TODO: Twój kod poniżej
zlote = float(input("Podaj kwotę w złotych: "))
euro = zlote / EUR_RATE
dolary = zlote / USD_RATE
print(f"{zlote:.2f} PLN = {euro:.2f} EUR")
print(f"{zlote:.2f} PLN = {dolary:.2f} USD")