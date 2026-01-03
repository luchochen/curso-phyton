nombres = [
    {"nombre": "ana", "nota1": 9,"nota2":7,"nota3":8},
    {"nombre": "juan", "nota1": 5,"nota2":4,"nota3":6},
    {"nombre": "pedro", "nota1": 7,"nota2":10,"nota3":6},
    {"nombre": "flor", "nota1": 3,"nota2":2,"nota3":1}
]


def nombre_estudiantes(lista):
    for estudiante in lista:
        print(estudiante["nombre"],
              estudiante["nota1"],
              estudiante["nota2"],
              estudiante["nota3"])

nombre_estudiantes(nombres)



def promedio_notas(notas):
    alumno_filtrado=[]
    for estudiante in notas:
        promedio=((
              estudiante["nota1"]+
              estudiante["nota2"]+
              estudiante["nota3"]
        )/3)
        print(estudiante["nombre"],"el promedio es: ",promedio)
        if promedio  >= 6:
            alumno_filtrado.append(estudiante["nombre"])
    print ("estos quedaron afuera por burros,:",alumno_filtrado)

promedio_notas(nombres)

def nota_mas_alta(lista):
    for estudiante in lista:
        nota=0
        if estudiante["nota1"]>estudiante["nota2"]and estudiante["nota3"]:
            nota=estudiante["nota1"]
        if estudiante["nota2"]>estudiante["nota1"]and estudiante["nota3"]:
            nota=estudiante["nota2"]    
        if estudiante["nota3"]>estudiante["nota1"]and estudiante["nota2"]:
            nota=estudiante["nota3"]
        print(estudiante["nombre"]+ " la nota mas alta fue ", nota)

nota_mas_alta(nombres)

def quien_tiene_mas_nota(lista):
    max_nota=0
    nombre=""
    for estudiante in lista:
        for nota in estudiante["nota1"],estudiante["nota2"],estudiante["nota3"]:
            if nota > max_nota:
                max_nota=nota
                nombre=estudiante["nombre"]
    print("la nota mas alta es",max_nota,"y es de...",nombre)

quien_tiene_mas_nota(nombres)

