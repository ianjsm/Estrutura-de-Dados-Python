import numpy as np

class VetorNaoOrdenado:
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao =  -1
        self.valores = np.empty(self.capacidade, dtype= int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio!")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])
    
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor está cheio!")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                print("Posição no vetor: ", i)
                return i
            else:
                print("Não encontrado no vetor")
                return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print("Esse número não existe no vetor")
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            
            self.ultima_posicao -= 1