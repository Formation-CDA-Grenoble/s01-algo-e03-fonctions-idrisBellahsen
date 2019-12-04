def cascadeDouble(list):
    # Début de ton code
    
    if isinstance(list,int):    
        return list*2  
    list2= []
    for number in list :
        if isinstance(number, int):
            list2.append(number*2)
        else:
            raise Exception("Ce n'est pas un nombre")
    return list2    
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], [2, 4, 6]),
    ([10], [20]),
    ([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]),
    ([-12, 0, 50], [-24, 0, 100]),
)

for test in tests:
    print(f"L'appel  cascadeDouble({test[0]})  renvoie: {cascadeDouble(test[0])} (résultat attendu: {test[1]})")



