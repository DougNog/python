while True:
    # Lê o nome de usuário
    usuario = input("Digite o nome de usuário: ")
    
    # Lê a senha
    senha = input("Digite a senha: ")
    
    # Verifica se a senha é igual ao nome de usuário
    if senha == usuario:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Cadastro realizado com sucesso!")
        break  # Sai do loop se a senha for válida
