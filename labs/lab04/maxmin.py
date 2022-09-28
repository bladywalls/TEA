maximo=0
minimo=0
primero= True
while True:
    try:
        inpu_str = input("Ingresar un numero:")
        if(inpu_str == "fin"):
            break
        else:
            if(primero):
                maximo= int(inpu_str)
                minimo= int(inpu_str)
                primero= False
            else:
                    if(int(inpu_str) > maximo): maximo = int(inpu_str)
                    if(int(inpu_str) < minimo): minimo = int(inpu_str)
    except:
        print("Valor no valido")
        continue
print("Maximo:", maximo)
print("Minimo:", minimo)