A = int(input("Escribeme el primer numero\n --> "))
B = int(input("Escribeme el segundo numero\n --> "))
C = int(input("Escribeme el tercer numero\n --> "))

msj  = str("El numero mas granade es: ")

while A == B or A == C or B == C:
    print("los numeros no deben ser iguales porfavor escriba numeros diferentes")
    A = int(input("Escribeme el primer numero\n --> "))
    B = int(input("Escribeme el segundo numero\n --> "))
    C = int(input("Escribeme el tercer numero\n --> "))


if A>B and A>C:
    print(msj, A)

if B>A and B>C:
    print(msj, B)
        
if C>B and C>A:
    print(msj, C)







