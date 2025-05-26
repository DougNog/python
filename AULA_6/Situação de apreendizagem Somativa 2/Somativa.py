# ==========================#
# INICIALIZAÇÃO DE LISTAS   #
# ==========================#

                 
rotas = []        # Lista para armazenar os nomes das rotas informadas pelo usuário. 
tempos = []       # Lista para armazenar o tempo (em segundos) de cada rota.         

# ==========================#
# ENTRADA DE DADOS INICIAL  #
# ==========================#

quantidade = int(input("Quantas rotas? "))
# Solicita ao usuário quantas rotas ele deseja cadastrar.                 
# O valor é convertido para inteiro para ser usado no laço de repetição.  

# ============================#
# COLETA DOS DADOS DAS ROTAS  #
# ============================#

for _ in range(quantidade):
    # Laço que repete o número de vezes indicado por "quantidade".  
    # A variável "_" é usada quando o índice não será necessário.   

    nome = input("Nome da rota: ")  
    # Solicita o nome da rota ao usuário.

    distancia = float(input("Distância (m): "))  
    # Solicita a distância da rota (em metros) e converte para número decimal.

    velocidade = float(input("Velocidade média (m/s): "))  
    # Solicita a velocidade média da rota (em metros por segundo) e converte para número decimal.

    tempo = distancia / velocidade  
    # Calcula o tempo necessário para percorrer a rota com base na fórmula: tempo = distância ÷ velocidade.

    rotas.append(nome)  
    # Adiciona o nome da rota à lista "rotas".

    tempos.append(tempo)  
    # Adiciona o tempo calculado à lista "tempos".

# ===================================#
# IDENTIFICAÇÃO DA ROTA MAIS RÁPIDA  #
# ===================================#

indice_mais_rapida = tempos.index(min(tempos))

# Encontra o menor tempo da lista "tempos" com a função min().               
# Depois, usa .index() para descobrir a posição desse menor tempo na lista.  
# O índice encontrado corresponde à rota mais rápida.                        


# =============================#
# EXIBIÇÃO DO RESULTADO FINAL  #
# =============================#

print(f"Rota mais rápida: {rotas[indice_mais_rapida]} ({tempos[indice_mais_rapida]} s)") 
# Exibe o nome da rota mais rápida e o tempo correspondente.  
# Usa f-string para formatar o texto com os dados corretos.   