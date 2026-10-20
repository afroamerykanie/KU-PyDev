# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Nie da się zbudować trójkąta")
else:
    if a == b == c:
        print("Trójkąt równoboczny")
    elif a == b or a == c or b == c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")

    najdluzszy = max(a, b, c)
    if najdluzszy == a:
        prostokatny = abs(a**2 - (b**2 + c**2)) < 1e-9
    elif najdluzszy == b:
        prostokatny = abs(b**2 - (a**2 + c**2)) < 1e-9
    else:
        prostokatny = abs(c**2 - (a**2 + b**2)) < 1e-9

    if prostokatny:
        print("Trójkąt prostokątny")