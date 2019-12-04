def double(number):
    # Début de ton code
    if isinstance(number, int):
        return number*2
    else:
       raise Exception("Ce n'est pas un nombre")

    # Fin de ton code



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -6),
)

for test in tests:
    print(f"L'appel  double({test[0]})  renvoie: {double(test[0])} (résultat attendu: {test[1]})")

print(double("a"))