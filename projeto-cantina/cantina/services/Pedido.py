from cantina.view.PaginaInicial import PaginaInicial

class Pedido:

    def __init__(self, produtos):
        nome = str(input("Oque você gostaria de pedir ?"))
        quant = int(input("Quantos"))

        for produto in produtos:
            if produto[0] == nome:
                self.pedidos.append([produto[0], quant, produto[2]])
                print("Pedido realizado.")
                break
