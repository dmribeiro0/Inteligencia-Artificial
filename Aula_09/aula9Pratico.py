from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        # Adiciona v se ele não existir no grafo
        if self.adj_list.get(v) is None:
            self.adj_list[v] = set()

    def add_edge(self, u, v):
        # Adiciona u ou v se eles não existirem no grafo
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_list[u].add(v)

    def get_order(self):
        # Retorna o número de vértices do grafo
        return len(self.adj_list)

    def get_size(self):
        # Retorna o número de arestas do grafo
        return sum(len(neigh) for neigh in self.adj_list.values())


def gen_neighbours(cell : tuple[int, int, int], max_missionaries : int):
    neighbours = []
    new_boat_side = 1 - cell[2]
    # Possiveis cargas do barco: (missionarios, canibais)
    moves = [(0, 1), (0, 2), (1, 1), (1, 0), (2, 0)]

    # Se o barco estiver na margem esquerda, pessoas saem da esquerda,
    # entao subtraimos do estado atual.
    if cell[2] == 0:
        moves = [(-x, -y) for (x, y) in moves]

    for dx, dy in moves:
        new_cell = (cell[0] + dx, cell[1] + dy, new_boat_side)
        m_left, m_right = new_cell[0], max_missionaries - new_cell[0]
        c_left, c_right = new_cell[1], max_missionaries - new_cell[1]

        # Mantem apenas estados dentro dos limites [0, max_missionaries].
        if 0 <= m_left <= max_missionaries and 0 <= c_left <= max_missionaries:
            # Regra de seguranca: em cada margem, missionarios nao podem
            # ficar em minoria (a menos que nao haja missionarios na margem).
            if (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right):
                neighbours.append(new_cell)

    return neighbours

# Constrói o grafo de estados a partir do estado inicial usando busca em largura (BFS).
# Cada estado é representado como uma tupla (missionarios_esquerda, canibais_esquerda, lado_barco).
def build_graph(initial_state : tuple[int, int, int]):
    g = Graph()
    
    visited : set = set()
    queue : deque = deque()

    g.add_vertex(initial_state)
    visited.add(initial_state)
    queue.append(initial_state)

    while queue:
        current_cell = queue.popleft()
        neighbours = gen_neighbours(current_cell, initial_state[0])
        
        for neighbour in neighbours:
            if neighbour not in visited:
                g.add_vertex(neighbour)
                visited.add(neighbour)
                queue.append(neighbour)
            g.add_edge(current_cell, neighbour)
    
    return g


def find_path(graph: Graph, initial_state: tuple[int, int, int], final_state: tuple[int, int, int]):
    # BFS no grafo para encontrar o menor caminho em numero de travessias.
    queue: deque = deque([initial_state])
    visited: set = {initial_state}
    parent: dict = {initial_state: None}

    while queue:
        current = queue.popleft()

        if current == final_state:
            # Reconstrucao do caminho do destino ate a origem via mapa de pais.
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for neighbour in graph.adj_list.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = current
                queue.append(neighbour)

    return []

g = build_graph((3, 3, 0))
print(g.get_order())
print((0, 0, 1) in g.adj_list)
print(find_path(g, (3, 3, 0), (0, 0, 1)))