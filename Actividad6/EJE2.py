respuesta = str(input("Vamos a realizar una cuenta de 100 a 0, desea continuar?\n (Y)/(N)?---->"))
x = 101
while respuesta != "N" and respuesta != "Y": 
         respuesta = str(input("Disculpe, introduzca (Y) para realizar la cuenta y (N) para finalizar el programa... (Y)/(N)?---->"))          

while x != 0 and respuesta =="Y" :
    x=x-1
    print(x)
print("Muchas gracias, su programa a finalizado!!")
    
if respuesta == "N":
        print("Fin del programa")
        

              