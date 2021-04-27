class PaginaProdutos:

    def __init__(self, produtos):
        self.pedidos = []
        self.pedidos.append([produtos[0], 2])

    def listar_produtos(produtos):
        print(" _______________________________________________________________________________________")
        for p in enumerate(produtos):
            print("[%d] Categoria: %s Produto: %s Preço: %d" % (p[0] + 1, p[1][0], p[1][1], p[1][2]))
        print(" _______________________________________________________________________________________")
