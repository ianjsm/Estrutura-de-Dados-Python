import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_de_elementos = 0
        self.valores = np.empty(self.capacidade, dtype= int)

    def __fila_vazia(self):
        return self.numero_de_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_de_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("Fila está cheia")
            return
        #nao está completo
        
    def desenfileirar(self):
        if self.__fila_vazia():
            print("Fila está vazia")
            return
        
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        else:
            print(self.valores[self.inicio])