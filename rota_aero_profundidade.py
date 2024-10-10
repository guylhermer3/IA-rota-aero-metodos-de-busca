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

def busca_profundidade(grafo, inicio, destino, caminho=None, visitados=None):
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = set()

    visitados.add(inicio)

    if inicio == destino:
        return caminho

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            novo_caminho = busca_profundidade(grafo, vizinho, destino, caminho + [vizinho], visitados)
            if novo_caminho:
                return novo_caminho

    return None

if __name__ == "__main__":
    grafo = carregar_rotas('routes.csv')
    
    origem = input("Digite a origem: ").strip()
    destino = input("Digite o destino: ").strip()

    caminho = busca_profundidade(grafo, origem, destino)
    if caminho:
        print(f"Caminho encontrado: {caminho}")
    else:
        print("Caminho não encontrado.")
