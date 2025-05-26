# Sistema de Cadastro de Animais para Doação (sem JSON)

animais = []
proximo_id = 1

def cadastrar_animal():
    global proximo_id
    print("\n--- Cadastrar Animal ---")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")
    porte = input("Porte (pequeno, médio, grande): ")
    

    animal = {
        "id": proximo_id,
        "nome": nome,
        "especie": especie,
        "idade": idade,
        "porte": porte,
        
    }

    animais.append(animal)
    print(f"Animal ID {proximo_id} cadastrado com sucesso!\n")
    proximo_id += 1

def listar_animais():
    print("\n--- Lista de Animais ---")
    if not animais:
        print("Nenhum animal cadastrado.\n")
        return

    for animal in animais:
        print(f"ID: {animal['id']}")
        print(f"Nome: {animal['nome']}")
        print(f"Espécie: {animal['especie']}")
        print(f"Idade: {animal['idade']}")
        print(f"Porte: {animal['porte']}")
       

def atualizar_animal():
    print("\n--- Atualizar Animal ---")
    try:
        id_alvo = int(input("Digite o ID do animal a ser atualizado: "))
    except ValueError:
        print("ID inválido!\n")
        return

    for animal in animais:
        if animal['id'] == id_alvo:
            print("Deixe em branco para manter o valor atual.")
            nome = input(f"Nome ({animal['nome']}): ") or animal['nome']
            especie = input(f"Espécie ({animal['especie']}): ") or animal['especie']
            idade = input(f"Idade ({animal['idade']}): ") or animal['idade']
            porte = input(f"Porte ({animal['porte']}): ") or animal['porte']
           

            animal.update({
                "nome": nome,
                "especie": especie,
                "idade": idade,
                "porte": porte,
                
            })

            print("Animal atualizado com sucesso!\n")
            return

    print("Animal com esse ID não encontrado.\n")

def remover_animal():
    print("\n--- Remover Animal ---")
    try:
        id_alvo = int(input("Digite o ID do animal a ser removido: "))
    except ValueError:
        print("ID inválido!\n")
        return

    for animal in animais:
        if animal['id'] == id_alvo:
            animais.remove(animal)
            print("Animal removido com sucesso!\n")
            return

    print("Animal com esse ID não encontrado.\n")

def menu():
    while True:
        print("=== Sistema de Cadastro de Animais ===")
        print("1. Cadastrar Animal")
        print("2. Listar Animais")
        print("3. Atualizar Animal")
        print("4. Remover Animal")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_animal()
        elif opcao == "2":
            listar_animais()
        elif opcao == "3":
            atualizar_animal()
        elif opcao == "4":
            remover_animal()
        elif opcao == "5":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar o menu
menu()