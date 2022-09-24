temperaturas=[]
promedio=0
for i in range(5):
    temperatura=int(input(f"Digita la {i+1} temperatura"))
    temperaturas.append(temperatura)


for temperatura in temperaturas: 
    promedio=promedio+temperatura


print(f'El promedio fue {promedio / len (temperaturas)}')
