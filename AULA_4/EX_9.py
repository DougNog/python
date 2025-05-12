#somando numeros do intervalo informado LImitando o maior numero

inicio = int(input("informe o primeiro numero: "))
fim = int(input("informe o numero final: "))
salto = int(input("informe o salto: "))
texto = "Cálculo :"
soma = 0
for numero in range (inicio, fim, salto):
    soma = soma + numero
    texto = texto + str(numero)
    if numero > 50:
        break
    if numero != fim-1:
        texto = texto + "+" "\nPassou de 50"
        print(f"{texto}")
        print(f"Soma: {soma}")