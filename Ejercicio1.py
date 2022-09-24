#funcion 
centinela = 0
centinela2 = 0
def calcularArea(largo, ancho):
    area = largo * ancho
    return area

largo = int(input("Ingrese el largo del Rectangulo: "))
ancho = int(input("Ingrese el ancho del Rectangulo: "))

area = calcularArea(largo,ancho)
for i in range(area):
    grafica = (area * "*")
    print (grafica)
print(f'El area de su Rectangulo es {area}')

#PERIMETRO

def calcularPerimetro(largo,ancho):
    perimetro=largo+largo+ancho+ancho
    print(f'EL Perimetro del rectangulo es {perimetro}') 

#Se solicita datos y se llama a la funcion

largo= int (input("ingrese el largo del Rectangulo"))
ancho= int (input("ingrese el ancho del Rectangulo"))

calcularPerimetro(largo,ancho)



