# Programa que lê 10 números inteiros e exibe o maior, o menor e a média

maior = None
menor = None
soma = 0

print("Digite 10 números inteiros:")

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

media = soma / 10

print("\nResultados:")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média: {media:.2f}")
