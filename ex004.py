"""
    Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
    foram lidas. Imprima as consoantes
"""
consoantes = []

for c in range(1,11):
    l = str(input(f'Digite o {c}º caractere: '))
    if l != 'a' and l != 'e' and l != 'i' and l != 'o' and l != 'u':
        if l != 'A' and l != 'E' and l != 'I' and l != 'O' and l != 'U':
            consoantes.append(l)
print(f'As consoantes digitadas foram {consoantes}.')