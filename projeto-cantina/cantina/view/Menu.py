
class Menu:
    opcao = 0

    def __init__(self):
        print("\n ------ Menu Principal ---------------------------------------------------------------")
        rotas = ['Página Inicial', 'Produtos', 'Fazer Pedido', 'Administração', 'Contato', 'Sair']
        for r in enumerate(rotas):
            print("[%d] %s" % (r[0] + 1, r[1]))
        self.opcao = int(input("digite sua escolha: "))
        return self.opcao
