print("calculadora basica")
print("para terminar ingrese fin")
print("las cuentas que podemos hacer son suma / resta / dividir / multiplicar")

palabra = ""

while palabra != "fin" : 

    deseo= input("que cuenta vamos a hacer?")
    if deseo == "fin" :
        break
    
    numero1 = float(input("ingrese un numero"))
    numero2 = float(input("ingrese otro numero"))

    if deseo == "suma":
        print("tu resultado es " , numero1 + numero2)
    if deseo == "resta":
        print("el resultado es", numero1 - numero2)
    if deseo == "multiplicar":
        print("tu resultado es",numero1 * numero2)
    if deseo == "dividir":
        print("tu resultado es",numero1 / numero2)
    palabra = input("escriba fin para terminar o ENTER para continuar")


print("programa terminado")
