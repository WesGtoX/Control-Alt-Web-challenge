string = input("Digite: ")

def number_string(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

if number_string(string) == True:
    print("A string '{0}' contém apenas números!".format(string))
else:
    print("A string '{0}' NÃO contém apenas números!".format(string))