#funcion 
centinela = 0
def calcularArea(largo, ancho):
    area = largo * ancho
    return area

largo = int(input("Ingrese el largo del Rectangulo: "))
ancho = int(input("Ingrese el ancho del Rectangulo: "))

area = calcularArea(largo,ancho)
for i in range(area):   
    print("*")
print(f'El area de su Rectangulo es {area}')



