suma = 0
total = 0
num = int(input("introduce un numero, cuando quiera terminar escriba 0. Realizaremos la mediana aritmetica:\n ---->"))

while num > 0:
    num = int(input("introduce otro numero:\n ---->"))
    if num > 0:
        suma = suma+num
        total = total+1
print(f"La mediana aritmetica es: {suma/total-0.5}")