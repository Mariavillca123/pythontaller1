print("Vamos a convertir tu temperatura")
temperaturas = int(input("Elige 1 si esta en celsius y 2 si esta en farenheit: "))
if temperatura ==1:
    celsius= float(input("Ingrese temperatura: "))
    Cfarenheit= (celsius * 9/5)+32
    print("Su temperatura en farenheit es: ",Cfarenheit)
elif temperatura ==2:
    farenheit= float(input("Ingrese temperatura:"))
    Ccelsius= (farenheit - 32)* 5/9
    print("Su temperatura en celsius es: ", Ccelsius)
else:
    print("error de ingreso")
