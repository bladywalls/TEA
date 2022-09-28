def calculopago(horas, tarifa):
    MAX_HORAS = 40
    horas_extras = 0
    if (horas > MAX_HORAS):
     horas_extras = horas - MAX_HORAS
    calculo = (horas * tarifa) + (horas_extras * (tarifa / 2))
    return calculo 

try: 
    horas = float(input ("Ingrese numero de horas:"))
    tarifa = float(input ("Ingrese tarifa:"))
    pago = calculopago(horas, tarifa)
    print(pago)

except: 
    print("ERROR! Valor ingresado no es valido")