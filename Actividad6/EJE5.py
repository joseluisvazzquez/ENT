sum = 0
total = 0
maximo = 0
minimo = 0
num = int(input("Escribe un numero:\n ---->"))
while num>0:
    num = int(input("Escribe un numero:\n ---->"))
    if num>0:
        sum = sum+num
        total = total+1
    if num > maximo:
        maximo = num
        minimo = num
    if num < minimo:
        minimo = num

print(f"La mediana aritmetica es: {sum/total}")
print(f"El minimo es: {minimo}")
print(f"El maximo es: {maximo}")