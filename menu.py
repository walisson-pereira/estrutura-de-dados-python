from arvore import Arvore


def main():

    livraria = Arvore("Livros")
    livraria.raiz.inserir_filho("Gastronomia")
    livraria.raiz.inserir_filho("Informática")
    livraria.raiz.inserir_filho("Engenharia")
    livraria.imprimir()

    encontrado = livraria.localizar_nodo("Livros")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_nodo("Informática")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_nodo("Letras")
    print("Encontrado: {}".format(encontrado))

    livraria.inserir_nodo("Informática","Linguagens")
    livraria.inserir_nodo("Linguagens", "Python")
    livraria.inserir_nodo("Gastronomia", "Culinária")
    livraria.inserir_nodo("Gastronomia", "Bebidas")
    livraria.imprimir()

    removido = livraria.remover_nodo("Bebidas")
    print("Removido: ", removido)
    removido = livraria.remover_nodo("Informática")
    print("Removido: ", removido)
    livraria.imprimir()

main()