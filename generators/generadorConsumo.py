import random

def generarDatos():
    datos = []
    for i in range(5000): #rango 1 a 5000
        dato={}
        id=random.randint(1,1000) #entero aleatorio entre 1 y 1000
        referencia=random.choice(['ACH01', 'ACH22', 'ACH43']) #listado de opciones
        marca=random.choice(['Sony','Rico', 'Kalley'])
        capacidad=random.randint(100,2000) #aleatorio entre 100 y 2000
        ciudad=random.choice(['Medellín', 'Bello', 'Envigado', 'Sabaneta', 'Itagüí'])
        responsable=random.choice(['Juan Pablo Muñetón', 'Daniela Muñetón', 'Andrés Felipe Muñetón', 'Gina Milena Muñetón', 'Mario Muñetón'])

        dato=[id, referencia, marca, capacidad, ciudad, responsable]
        datos.append(dato)

    return datos

print(generarDatos())
