#PERIMETRO

def calcularPerimetro(largo,ancho):
    perimetro=largo+largo+ancho+ancho
    print(f'EL Perimetro del rectangulo es {perimetro}') 

#Se solicita datos y se llama a la funcion

largo= int (input("ingrese el largo del Rectangulo"))
ancho= int (input("ingrese el ancho del Rectangulo"))

calcularPerimetro(largo,ancho)
