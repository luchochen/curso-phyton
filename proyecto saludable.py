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
        


        

