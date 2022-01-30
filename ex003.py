"""
    Faça um Programa que leia 4 notas, mostre as notas e a média na tela
"""
notas = []
for c in range(1,5):
    notas.append(float(input(f'Digite a {c}º nota: ')))
print(f'A media do aluno é {sum(notas)/4:.2f}.')