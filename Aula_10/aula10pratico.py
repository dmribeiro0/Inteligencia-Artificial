from typing import List, Tuple

# Capacidade do caminhao (em m^3)

# Numero de bairros

# Volume de coleta por bairro (em m^3)

# Matriz de distancias entre os bairros (em km)

# Genotipo representado como uma sequencia de bairros a serem visitados (nao pode ultrapassar a capacidade do caminhao)

genotipo: List[int]

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
def avaliar_aptidao(solucao: List[int]) -> float:
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
def mutacao(individuo: List[int]) -> List[int]:
    return []