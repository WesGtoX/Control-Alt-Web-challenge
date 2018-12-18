array = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9]

def find_duplicate(arr):
    lista = []
    dupli = []
    for x in arr:
        if x not in lista:
            lista+= [x]
        else:
            if x not in dupli:
                print("Número duplicado: {0}".format(x))
            dupli+= [x]

find_duplicate(array)