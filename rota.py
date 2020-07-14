from lista_ligada import ListaLigada, Celula


class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'{self.nome}\n {self.endereco}'

def main():
    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("Hortifruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")
    loja4 = Loja("Supermercado", "Alameda Santos, 400")
    loja5 = Loja("Mini Mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")

    lista = ListaLigada()

    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir_no_inicio(loja3)

    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)

    print(lista.quantidade)
    lista.imprimir()

    print("")

    removido = lista.remover_do_inicio()
    print("Removido {}".format(removido))
    removido = lista.remover_do_inicio()
    print("Removido {}".format(removido))

    print("")
    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover(2)
    print("")
    print(lista.quantidade)
    lista.imprimir()
    print("Removido da posicao 2: {}".format(removido))

    removido = lista.remover(2)
    print("")
    print(lista.quantidade)
    lista.imprimir()
    print("Removido da última posição: {}".format(removido))

    removido = lista.remover(0)
    print("")
    print(lista.quantidade)
    lista.imprimir()
    print("Removido do início: {}".format(removido))

    print('Item 0')
    print(lista.item(0))

main()
