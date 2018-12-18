str1 = input("Digite a primeira palavra: ")
str2 = input("Digite a segunda palavra: ")

def anagrama(s):
    stri_anag = ""
    i = len(s) - 1
    while i >= 0:
        stri_anag+= s[i]
        i-=1
    return stri_anag

def compar(x, y):
    if x == y:
        print("As duas strings SÃO anagramas!!")
    else:
        print("As duas strings NÃO são anagramas!!")

compar(str1, anagrama(str2))