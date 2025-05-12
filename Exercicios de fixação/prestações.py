valor = int(input("Digite o valor da compra: "))
prestacao = int(input("Digite o número de prestações: "))

valor_prestacao = valor / prestacao
print(f"Valor de cada prestação: R$ {valor_prestacao:.2f}")