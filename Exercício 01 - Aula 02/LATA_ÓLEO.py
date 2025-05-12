#Crie um programa e declare uma constante PI (use 4 casas após a vírgula). Dados o raio e a altura, calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: volume = PI * r 2 * altura

PI = 3.1415
raio = float(input("Digite o raio da lata de óleo: "))
altura = float(input("Digite a altura da lata de óleo: "))

volume = PI * (raio ** 2) * altura
print(f"O volume da lata de óleo é: {volume:.4f} m³")

