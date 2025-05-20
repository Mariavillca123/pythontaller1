def tiempo(horas_ingresadas):
    dias = int(horas_ingresadas/24)
    horas = int(horas_ingresadas % 24)
    minutos = int((horas_ingresadas * 60) %60)
    segundos = int((horas_ingresadas *3600) %60)
    
    return dias, horas, minutos, segundos
    
try:
    horas_usuario = float(input("Ingrese las horas: "))
    dias, horas, minutos, segundos = tiempo(horas_usuario)
    
    print(f"Tiene {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos. ")
    
except:
    print("Las horas se ingresan en valor numérico...")
