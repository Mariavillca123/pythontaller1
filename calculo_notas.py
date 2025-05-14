print("Ingresa las notas, para detener el ingreso escriba fin")
suma=0
contador=0
while True:
    nota= input("Nota: ")
    if nota != "fin":
        suma= suma+float(nota)
        contador= contador+1
    else:
        if contador>0:
            promedio= suma/contador
            print("Su promedio es: ",promedio)
        else:
            print("No hay notas...")
        break
