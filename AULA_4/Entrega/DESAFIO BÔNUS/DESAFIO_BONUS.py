# Solicita o número para treinar a tabuada
numero = int(input("Digite o número que você quer treinar a tabuada: "))

# Inicializa contadores de acertos e erros
acertos = 0
erros = 0

# Loop de 1 a 10 para a tabuada
for i in range(1, 11):
    resposta = int(input(f"{numero} x {i} = "))
    resultado_correto = numero * i

    if resposta == resultado_correto:
        print("CORRETO\n")
        acertos += 1
    else:
        print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {resultado_correto}\n")
        erros += 1

# Exibe o total de acertos e erros
print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")
