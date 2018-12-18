array = [0, 1, 2, 3, 4, 6, 7, 8, 9]

def faltante(arr):
    i = 0
    for x in arr:
        if x != i:
            while(i != x):
                print("Número faltante: {0}".format(i))
                i += 1
            i += 1
        else:
            i += 1

faltante(array)