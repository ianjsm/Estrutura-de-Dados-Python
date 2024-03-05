import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.chararray(self.__capacidade, unicode=True)

    def pilha_cheia(self):
        return self.__topo == self.__capacidade - 1

    def pilha_vazia(self):
        return self.__topo == -1

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("Pilha cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha vazia")
        else:
            self.__topo -= 1
    
    def ver_topo(self):
        if not self.pilha_vazia():
            return self.__valores[self.__topo]
        else:
            return -1

expressao = input("Digite a expressão: ")
pilha = Pilha(len(expressao))

for caractere in expressao:
    if caractere in "({[":
        pilha.empilhar(caractere)
    elif caractere in ")}]":
        if (caractere == ")" and pilha.ver_topo() == "(") or \
           (caractere == "}" and pilha.ver_topo() == "{") or \
           (caractere == "]" and pilha.ver_topo() == "["):
            pilha.desempilhar()
        else:
            print("Erro!")
            break
else:
    if pilha.pilha_vazia():
        print("A expressão digitada é válida!")
    else:
        print("Erro!")