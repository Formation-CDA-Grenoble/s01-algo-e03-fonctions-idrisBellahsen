def cascadeIsGreater(list, number):
    # Début de ton code
    list2= []
    for x in list:
        if isinstance(number, int):  
            if x < number :
                list2.append(False)
            elif x > number:
                list2.append(True)   
            else :
                list2.append(None)
        else:
            raise Exception("Ce n'est pas un nombre")        
    return list2         
   
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 2, [False, True, True]),
    ([1, 2, 3], 4, [False, False, False]),
    ([-12, 0, 50], 0, [False, True, True]),
    ([1, 1, 1], 1, [True, True, True]),
)

for test in tests:
    print(f"L'appel  cascadeIsGreater({test[0]}, {test[1]})  renvoie: {cascadeIsGreater(test[0], test[1])} (résultat attendu: {test[2]})")
