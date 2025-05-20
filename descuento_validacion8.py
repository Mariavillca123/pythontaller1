def calculo_precio(precio, descuento):
    return precio *(1-descuento/100)
        
try:
    precio = float(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento: "))
    
    if 0<= descuento <= 100:
        resultado = calculo_precio(precio, descuento)
        print(f"El precio final es: {resultado}")
    else:
        print("El descuento no esta entre 0 y 100 !!")
except:
    print("Ingrese valores numéricos...")
