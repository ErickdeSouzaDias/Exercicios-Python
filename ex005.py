"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""
numeros = []
pares = []
impares = []

for c in range(0, 20):
    numeros.append(float(input(f'Digite o {c+1}º número: ')))
    if numeros[c]%2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
print(f'Numeros digitados: {numeros}')
print(f'Números PARES: {pares}')
print(f'Números IMPARES: {impares}')
