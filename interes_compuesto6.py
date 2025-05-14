P= float(input("ingrese el capital inicial: "))
r= float(input("ingrese la tasa de interes: "))
t= int(input("ingrese el numero de año: "))

interes_compuesto= P*(pow((1+r), t))
print(interes_compuesto)
