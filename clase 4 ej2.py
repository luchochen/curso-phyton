def es_par(numero):
    if numero %2==0:
        return "true es par"
    else:
        return "false es impar"
    
x=es_par(43)
print(x)


def tabla_multiplicar(n):
    
    for i in range (1,11):
        producto=i * n
        print(n,"x",i,"=",producto)
    
a=tabla_multiplicar(2)
print(a)


def mayor_de_tres(a,b,c):
    
        if a > b and a > c:
            return (f"el mayor es {a}")
        if b > a and b > c:
            return (f"el mayor es {b}")
        if c > a and c > b :
            return (f"el mayor es{c}")
        

y=mayor_de_tres(10,199,20)
print(y)