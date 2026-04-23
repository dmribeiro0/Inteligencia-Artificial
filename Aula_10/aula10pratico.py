from typing import List, Tuple

# Genotipo representado como uma sequencia de bairros a serem visitados (nao pode ultrapassar a capacidade do caminhao)
genotipo: List[int]

#### Capacidade do caminhao (em m^3) ####
capacidade_caminhao: int
# capacidade_caminhao = int(input("Digite a capacidade do caminhão em m^3: "))
capacidade_caminhao = 8

#### Numero de bairros ####
num_bairros: int
# num_bairros = int(input("Digite o número de bairros: "))
num_bairros = 12

#### Volume de coleta por bairro (em m^3) ####
volumes_bairros : List[int] = []
# for i in range(int(num_bairros)):
#     volume_bairro = input(f"Digite o volume de coleta para o bairro {i+1} em m^3: ")
#     volumes_bairros.append(int(volume_bairro))
volumes_bairros = [2, 1, 3, 2, 1, 3, 1, 2, 3, 1, 2, 1]

#### Matriz de distancias entre os bairros (em km) ####
distancias : List[List[int]] = []
# for i in range(int(num_bairros)):
#     linha = []
#     for j in range(int(num_bairros)):
#         distancia = input(f"Digite a distância entre o bairro {i+1} e o bairro {j+1} em km: ")
#         linha.append(float(distancia))
#     distancias.append(linha)
distancias = [
    [0, 5, 9, 14, 7, 6, 12, 11, 8, 10, 13, 15],
    [5, 0, 4, 12, 6, 5, 11, 13, 9, 8, 14, 10],
    [9, 4, 0, 6, 10, 8, 12, 9, 7, 11, 13, 14],
    [14, 12, 6, 0, 8, 7, 9, 10, 12, 13, 5, 6],
    [7, 6, 10, 8, 0, 5, 8, 11, 10, 9, 12, 13],
    [6, 5, 8, 7, 5, 0, 6, 9, 8, 10, 11, 14],
    [12, 11, 12, 9, 8, 6, 0, 4, 7, 8, 10, 9],
    [11, 13, 9, 10, 11, 9, 4, 0, 3, 6, 7, 8],
    [8, 9, 7, 12, 10, 8, 7, 3, 0, 5, 9, 10],
    [10, 8, 11, 13, 9, 10, 8, 6, 5, 0, 4, 7],
    [13, 14, 13, 5, 12, 11, 10, 7, 9, 4, 0, 3],
    [15, 10, 14, 6, 13, 14, 9, 8, 10, 7, 3, 0]
]


# ================================================= #
# =============== Algoritmo Genetico ============== #
# ================================================= #


# Gerar populacao inicial
# De forma aleatoria, sem consideracoes adicionais
def gerar_populacao_inicial(qtd_bairros: int, tam_populacao: int) -> List[List[int]]:
    populacao_inicial = []
    return populacao_inicial

# Avaliar a aptidao de cada solucao
# Consideracoes:
# - Distancia total percorrida (quanto menor, melhor)
# - Capacidade do caminhao (nao pode ser ultrapassada)
# - Numero excessivo de viagens (quanto menor, melhor)
def avaliar_aptidao(solucao: List[int], 
                    distancias: List[List[int]], 
                    capacidade_caminhao: int, 
                    volumes_bairros: List[int]) -> float:
    aptidao = 0.0
    return aptidao

# Selecionar os pais para a reproducao
# Seleciona as solucoes com melhores aptidoes, mas inclui uma componente de aleatoriedade para manter a diversidade
def selecionar_pais(populacao: List[List[int]], aptidoes: List[float]) -> List[List[int]]:
    pais = []
    return pais

# Realizar crossover para gerar novos individuos
# Escolhe o meio como ponto de crossover e combina as partes dos pais
def crossover(pai1: List[int], pai2: List[int]) -> Tuple[List[int], List[int]]:
    return [], []

# Realizar mutacao para introduzir variabilidade
# Realiza uma troca aleatoria entre dois bairros na sequencia do individuo
def mutacao(solucao: List[int]) -> List[int]:
    return []

# Escolhe a melhor solucao apos todas as geracoes (iteracoes)
def algoritmo_genetico(qtd_bairros: int, 
                       tam_populacao: int, 
                       distancias: List[List[int]], 
                       capacidade_caminhao: int, 
                       volumes_bairros: List[int]) -> List[int]:
    return []