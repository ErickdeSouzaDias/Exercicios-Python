"""
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
"""
lista = []
for c in range(1,6):
    lista.append(int(input(f'Digite o {c}º número:')))
print('Os numeros digitados foram: ')

for d in range(0,5):
    print(f'{lista[d]} ', end="")