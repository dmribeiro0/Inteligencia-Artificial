# Atividade Prática 09

## Descrição
Implemente um programa que resolva o problema clássico dos missionários e canibais utilizando algoritmos de busca (como busca em largura, ou busca em profundidade, ou busca A*, etc). 

## Solução
A solução foi modelada como um **grafo de estados** do problema.

Cada vértice representa uma configuração no formato:
- `(M_esq, C_esq, B)`
- `M_esq`: número de missionários na margem esquerda
- `C_esq`: número de canibais na margem esquerda
- `B`: lado do barco (`0` para esquerda, `1` para direita)

As arestas representam uma travessia válida do barco entre dois estados. Para gerar os próximos estados, são considerados os movimentos possíveis do barco com capacidade de até duas pessoas:
- `(0,1)`, `(0,2)`, `(1,1)`, `(1,0)`, `(2,0)`

Em cada estado gerado, são aplicadas as restrições do problema:
- Quantidade de missionários e canibais deve permanecer no intervalo válido.
- Em nenhuma margem os missionários podem ficar em minoria em relação aos canibais, exceto quando não há missionários na margem.

Com isso, o programa constrói automaticamente o grafo completo de estados alcançáveis a partir do estado inicial `(3,3,0)`, utilizando uma exploração em largura (BFS) com fila e conjunto de visitados para evitar repetições.
