num = int(input("Escribeme un numero, sí es mayor a 0 calcularemos us cuadrado, sí es menor o igual nos dará error\n --->"))
if num <= 0:
    print("error")
else: 
    print("El cuadrado de tu numero es: ", num*num)