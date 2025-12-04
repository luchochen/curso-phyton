entrada = 3000
edad=int(input("ingrese su edad: "))
sala=input("elija la sala: 2d / 3d / 4d / imax: ")
dia=input("ingrese que dia de la semana quiere ver la pelicula: ")
tarjeta=input("tiene tarjeta socio? (si/no)")

#descuento_edad 

if edad < 12 :
    
    descuento= 0.4
    total_edad = entrada - (entrada * descuento)


elif 12 <= edad < 25 :
    
    descuento= 0.25
    total_edad = entrada - (entrada * descuento)

    

elif 25 <= edad < 65 :
    descuento= 0
    total_edad = entrada - (entrada * descuento)
    
else:
    print("tiene un 30% descuento")
    descuento= 0.3
    total_edad = entrada - (entrada * descuento)
   

#recargo_sala

if sala == "2d":
    print("sin recargo")

elif sala == "3d":
    print("tiene recargo de $800")
    recargo= +800
    total_sala= total_edad + recargo
    

elif sala == "4d":
    print("tiene recargo de $1500")
    recargo= +1500
    total_sala= total_edad + recargo
   

elif sala == "imax":
    print("tiene recargo de $1200")
    recargo= + 1200
    total_sala= total_edad + recargo
   

#descuento_dia
if dia == "martes" or dia == "miercoles":
    print("20% descuento del dia en la entrada")
    diaoff= 0.2
    descuento_dia = entrada * diaoff
    total_final= total_sala - descuento_dia

   

else :
    ("no hay descuento por dia")
    diaoff= 0
    descuento_dia = entrada * diaoff
    total_final= total_sala - descuento_dia
    

if tarjeta == "si":
    descuento_tarjeta = 0.15
    total_final_completo = total_final-(total_final * descuento_tarjeta)

if tarjeta == "no" :
    print("no hay descuento")
    descuento_tarjeta = 0
    total_final_completo = total_final-(total_final * descuento_tarjeta)
    


print("--SISTEMA DE VENTA DE ENTRADAS DE CINE--")
print("ENTRADA GENERAL: $3000 ")
print("descuentos por edad -",descuento * 100,"%")
print("recarga por sala +$",recargo)
print("descuento por dia:- ",  diaoff * 100,"%")
print("descuento por socio: ", descuento_tarjeta * 100,"%")
print ("total a pagar es: $",total_final_completo)


    

    
    

