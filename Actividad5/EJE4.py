Pass = str(input("Se necesita clave de acceso, introduzca el password:\n ---->"))
intentos = 3

while Pass != "eureka" and intentos > 1:
    intentos = intentos-1
    Pass = str(input(f"Tienes {intentos} de 3 intentos.\n introduzca  de nuevo el password:\n ---->"))

if Pass == "eureka":
    print("Felicidades!! Lo has conseguido!")
else:
    print("Se han agotado los intentos, cerrando programa.")
