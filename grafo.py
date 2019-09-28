from collections import deque
from collections import defaultdict


class Grafo:
    def __init__(self, NumVertice = None, NumAresta = None, ListaAdj = []):
        self.NumVertice = NumVertice
        self.NumAresta = NumAresta
        self.ListaAdj = defaultdict(list)
        self.inicializa()
        print(self.ListaAdj)

    # sobrecarga do operador 'toString()'
    # def __repr__(self):
    #     return str(self)
    # def __str__(self):
    #     return str(self)

    def inicializa(self):
        # abrindo o arquivo
        arquivoGrafo = open('problema1.txt', 'r')
        self.leituraDoArquivo(arquivoGrafo)

    def leituraDoArquivo(self, arquivoGrafo):
        self.NumVertice = arquivoGrafo.readline()
        self.NumAresta = arquivoGrafo.readline()
        self.criarListaAdj(arquivoGrafo)
        
    def criarListaAdj(self, arquivoGrafo):
        for linhaArquivo in arquivoGrafo:
            uv = linhaArquivo.split(" ")
            u = uv[0]
            v = uv[1].split("\n")
            self.ListaAdj[u].append(v[0])

grafo = Grafo()
print(grafo)