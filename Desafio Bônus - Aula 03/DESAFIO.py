#Dada a atual crise hídrica do país, as pessoas começaram a construir reservatórios para armazenar água em suas propriedades. Faça um programa que auxilie os utilizadores do reservatório a controlarem seu consumo. Obtenha do teclado as dimensões de um reservatório (altura, largura e comprimento, em centímetros) e o consumo médio diário dos utilizadores do reservatório (em litros/dia). Assuma que o reservatório esteja cheio, tenha formato cúbico e informe:

#A capacidade total do reservatório, em litros;
#A autonomia do reservatório, em dias;
#A classificação do consumo, de acordo com a quantidade de dias de autonomia: Consumo elevado, se a autonomia for menor que 2 dias; Consumo moderado, se a autonomia estiver entre 2 e 7 dias; Consumo reduzido, se a autonomia maior que 7 dias.

#Obs.: Considere que cada litro equivale a 1000 cm³ ou 1 dm³

#Entrada de dados
altura = float(input("Digite a altura do reservatório em cm: "))
largura = float(input("Digite a largura do reservatório em cm: "))
comprimento = float(input("Digite o comprimento do reservatório em cm: "))

consumo_medio_diario = float(input("Digite o consumo médio diário em litros: "))

#Cálculo da capacidade total do reservatório em litros
capacidade_total_cm3 = altura * largura * comprimento
capacidade_total_litros = capacidade_total_cm3 / 1000

#Cálculo da autonomia do reservatório em dias
autonomia = capacidade_total_litros / consumo_medio_diario

#Classificação do consumo
if autonomia < 2:
    classificacao = "Consumo elevado"
elif 2 <= autonomia <= 7:
    classificacao = "Consumo moderado"
else:
    classificacao = "Consumo reduzido"

#Saída de dados
print(f"A capacidade total do reservatório é de {capacidade_total_litros:.2f} litros.")
print(f"A autonomia do reservatório é de {autonomia:.2f} dias.")
print(f"A classificação do consumo é: {classificacao}.")


