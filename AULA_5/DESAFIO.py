resposta = input("Você gosta de Python?: ")
while resposta != "sim" and resposta != "não":
    print("Resposta inválida. Por favor digite 's' ou 'n'.")
    resposta = input("Você gosta de Python? (s/n): ")
else:
        print("Ótimo! Python é uma linguagem poderosa.")