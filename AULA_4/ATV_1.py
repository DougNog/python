#Crie um programa em linguagem Python que utilize a estrutura de repetição for para encontrar e exibir todos os números pares no intervalo de 1 a 100

print("Números pares de 1 a 100:")

for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)