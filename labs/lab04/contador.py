total = 0
contador = 0
while True: 
        input_str = input("Ingrese un numero:")
        try:
            if(input_str == "fin"):
                break
            else: 
                total = total + int(input_str)
                contador = contador + 1
                promedio = total / contador 
        except:
                print("Valor no valido")
                continue 

print("Total:", total)
print("Contador:", contador)
print("Promedio:", promedio)