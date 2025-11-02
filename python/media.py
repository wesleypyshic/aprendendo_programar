Numeros = [7, 10,5,8,4,8]
pesos = [5, 2,3,1,6,0]

# media simples
denomidor = len(Numeros)
soma = sum(Numeros) 
mediasimples = soma/denomidor
print(mediasimples)

# media ponderada
somap = sum(pesos)
soma2 = 0
for numero, peso in zip(Numeros, pesos):
    produto = numero * peso
    soma2 += produto
    mediap = soma2/somap
    
print('media simples:', mediasimples, 'meida ponderada:', mediap)

media = 7

if mediasimples, mediap >= media:
    print('aprovado')
else:
    print('reprovado')