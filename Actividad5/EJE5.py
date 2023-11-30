n = int(input("Introduce un numero para hacer su factorial:\n ---->"))
f = 1 
for i in range(1,n+1):
    print(i)
    f = f*i
print(f"!({n})= {f}")
