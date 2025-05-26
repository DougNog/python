bancos = ["Banco do Brasil", "Caixa", "Santander"]
print(bancos)
#Resultado: ['Banco do Brasil', 'Caixa', 'Santander']
bancos[1] = "Itaú"
print(bancos)
#Resultado: ['Banco do Brasil', 'Itaú', 'Santander']
bancos[-1] = "C6"
print(bancos)
#Resultado: ['Banco do Brasil', 'Itaú', 'C6']
#----------------------------------------------------------------------------------------------------------------------------------------##-----------------------------------------------------------ADICIONAR--------------------------------------------------------------------#
print(bancos)
#Resultado: ['Banco do Brasil', 'Itaú', 'C6']
bancos = bancos + ["Bradesco", "Nubank"]
print(bancos)
#Resultado: ['Banco do Brasil', 'Itaú', 'C6', 'Bradesco', 'Nubank']
bancos += ["Safra"]
print(bancos)
#Resultado: ['Banco do Brasil', 'Itaú', 'C6', 'Bradesco', 'Nubank', 'Safra']
#----------------------------------------------------------------------------------------------------------------------------------------##-----------------------------------------------------LISTA DENTRO DE OUTRA LISTA--------------------======------------------------------#
compra = [10.2, 3.35, 16.3, ["tomate", "sabonete", "arroz"]]
print(compra)
produtos = compra[3]
print(produtos)
total = compra[0] + compra[1] + compra[2]
print(total)
letra = ["a", "b", "c"]
num = [2,4,6]
tudo = [letra + num]
print(tudo)
print(f"letras: {tudo[0]}")
print(f"números: {tudo[1]}")
#----------------------------------------------------------------------------------------------------------------------------------------##-----------------------------------------------------------LEN e INDEX------------------------------------------------------------------#
letras = ["a", "b", "c",]
print(f"tamanho da lista: {len(letras)}")
print(f"endereço da letra 'b': {letras.index('b')}")
#----------------------------------------------------------------------------------------------------------------------------------------##--------------------------------------------------VERIFICANDO A EXISTENCIA DE UM ITEM NA LISTA------------------------------------------#
letras = ["a", "b", "c", "d", "e", "f"]
var = input("Digite uma letra: ")
if var.lower() in letras:
    print(f"A letra '{var.lower()}'está na lista.")
else:
    print(f"A letra '{var.lower()}' não está na lista.")
#----------------------------------------------------------------------------------------------------------------------------------------##-------------------------------------------------ADICIONAR ELEMENTOS FORNECIDOS PELO USUÁRIO--------------------------------------------#
nova = []
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break   
    nova.append(num)
    print(nova)
    

#----──▒▒▒▒▒────▄████▄─────-----#
#----─▒─▄▒─▄▒──███▄█▀────── ----#
#----─▒▒▒▒▒▒▒─▐████──█──█──-----#
#----─▒▒▒▒▒▒▒──█████▄──────-----#
#----─▒─▒─▒─▒───▀████▀─────-----#


