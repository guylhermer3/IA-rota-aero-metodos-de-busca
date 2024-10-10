from collections import deque
import pandas as pd
from collections import defaultdict

def carregar_rotas(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    grafo = defaultdict(list)
    for _, linha in df.iterrows():
        origem = linha['AER']
        destino = linha['KZN']
        grafo[origem].append(destino)
    return grafo

def busca_largura(grafo, inicio, destino):
    visitados = set()
    fila = deque([[inicio]])

    while fila:
        caminho = fila.popleft()
        no = caminho[-1]

        if no not in visitados:
            vizinhos = grafo[no]

            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

                if vizinho == destino:
                    return novo_caminho

            visitados.add(no)

    return None

if __name__ == "__main__":
    grafo = carregar_rotas('routes.csv')
    
    origem = input("Digite a origem: ").strip()
    destino = input("Digite o destino: ").strip()
    
    caminho = busca_largura(grafo, origem, destino)
    if caminho:
        print(f"Caminho encontrado: {caminho}")
    else:
        print("Caminho não encontrado.")
        