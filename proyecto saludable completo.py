print("=== MI ASISTENTE SALUDABLE ===")
print("1. Calcular IMC")
print("2. Calorías de una comida")
print("3. Analizar horas de sueño")

opcion= int(input("ingrese una opcion: "))


match opcion:
    case 1:
        print("--CALCULAR IMC--")
        nombre=input("ingrese su nombre: ")
        peso=float(input("ingrese su peso: "))
        altura=float(input("ingrese su altura en m: "))

        imc = peso / (altura * altura)

        print ("tu IMC es :", imc)

        if imc < 18.5 :
            print("bajo peso")
        elif 18.5 <= imc < 24.9:
            print("peso normal")
        elif 25 <= imc < 29.9:
            print("sobre peso")
        else:
            print("obesidad")


    case 2:
        print("--CALORIAS DE UNA COMIDA--")
        print("   OPCIONES DE COMIDA \n       elija una: ")
        print("1- manzana (52 calorias)")
        print("2. banana (85 cal)")
        print("3. empanada de carne( 250 cal)")
        print("4- pizza 210")
        print("5- yogurt 59")

        opcion=int(input("elija un numero: "))
        cantidad=int(input("ingrese cuantas porciones quiere: "))


        match opcion:
            case 1: 
                comida= "manzana"
                calorias= (52 * cantidad)
                precio= (500 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 2: 
                comida= "banana"
                calorias= (85 * cantidad)
                precio= (800 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 3: 
                comida= "empanada"
                calorias= (252 * cantidad)
                precio= (2500 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 4: 
                comida= "pizza"
                calorias= (210 * cantidad)
                precio= (1900 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 5: 
                comida= "yogurth"
                calorias= (59 * cantidad)
                precio= (700 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")

        opcion=int(input("elija un numero: "))
        cantidad=int(input("ingrese cuantas porciones quiere: "))
                
        match opcion:
            case 1: 
                comida= "manzana"
                calorias= (52 * cantidad)
                precio= (500 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 2: 
                comida= "banana"
                calorias= (85 * cantidad)
                precio= (800 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 3: 
                comida= "empanada"
                calorias= (252 * cantidad)
                precio= (2500 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 4: 
                comida= "pizza"
                calorias= (210 * cantidad)
                precio= (1900 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")
            case 5: 
                comida= "yogurth"
                calorias= (59 * cantidad)
                precio= (700 * cantidad)
                efectivo=( precio * 0.2)
                print("$-",efectivo,"descuento en efectivo")
                total= precio - efectivo
                print("si comes",cantidad,"de",comida,"sera un total de: $",total, "y consumes",calorias,"calorias")


    case 3:
        print("--ANALISIS DE SUEÑO--")

        print("ingrese fin para terminar")

        horas_dormidas=""
        horas =""

        while horas_dormidas != "fin" :
            
            horas_dormidas=input ("ingrese la cantidad de horas que duerme: ")
            
            if horas_dormidas == ("fin"):
                print("terminado")
                break

            horas = float(horas_dormidas)


            if horas  < 6 :
                print("dormiste poco")
            

            elif horas > 8:
                print("dormiste bastante")
                
            
            else:
                print("buen descanso")

        print("programa terminado")