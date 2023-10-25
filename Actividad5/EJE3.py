d = int(input("Introduceme el dia deseado:\n --->"))
m = int(input("Introduceme el mes deseado:\n --->"))
meses = ["null","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

while d > 31 or d <= 0 and m > 12 or m <= 0:
    print("Formato erroneo, porfavor vuelva a introducir el dia  el mes... ")
    d = int(input("Introduceme el dia deseado:\n --->"))
    m = int(input("Introduceme el mes deseado:\n --->"))
    if d <= 31 or d > 0 and m <= 12 or m > 0:
        break

print(d, "de", meses[m])