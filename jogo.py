from pilha import Pilha

class Fase:
    def __init__(self, cenario, pontuacao, punicao):
        self.cenario = cenario
        self.pontuacao = pontuacao
        self.punicao = punicao

    def __repr__(self):
        return self.cenario

def main():
    fases = Pilha()
    fase1 = Fase("Floresta", 300, -100)
    fase2 = Fase("Castelo", 100, -4)
    fase3 = Fase("Caverna", 400, -50)
    fase4 = Fase("Guerra", 3000, -400)

    fases.empila(fase1)
    fases.empila(fase2)
    fases.empila(fase3)
    fases.empila(fase4)
    falhou = fases.desempilha()
    print("Falou na fase:")
    print(falhou)
    falhou = fases.desempilha()
    print("Falou na fase:")
    print(falhou)
    print("Voltou para a fase")
    print(fases.topo)





main()