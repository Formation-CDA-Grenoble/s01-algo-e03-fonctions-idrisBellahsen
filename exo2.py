def conditionalDouble(number):
    # Début de ton code
      # Début de ton code
    if isinstance(number, int):
        if(number>0):
            return number*2
        else:
            return number
    else:
       raise Exception("Ce n'est pas un nombre")

    # Fin de ton code



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -3),
)

for test in tests:
    print(f"L'appel  conditionalDouble({test[0]})  renvoie: {conditionalDouble(test[0])} (résultat attendu: {test[1]})")
print(conditionalDouble("a"))