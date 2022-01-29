"""
    Faça um Programa que leia um vetor de 10 números reais e mostre-os
    na ordem inversa.
"""

lista = []
for c in range(1,11):
    lista.append(int(input(f'Digite o {c}º número:')))
lista.reverse()
print('Os numeros digitados foram: ')

for d in range(0,10):
    print(f'{lista[d]} ', end="")