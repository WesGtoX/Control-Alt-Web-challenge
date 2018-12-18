array = [0, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9]

def find_duplicate(arr):
    lista = []
    dupli = []
    for x in arr:
        if x not in lista:
            lista+= [x]
    print("Lista sem números duplicados: {0}".format(lista))

find_duplicate(array)