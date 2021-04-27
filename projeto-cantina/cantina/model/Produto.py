class Produto:
    produtos = [()]

    def __init__(self):
        self.produtos = [('pastel de frango', 'salgado frito', 7),  # (descricao, categoria, valor)
                         ('coxinha', 'salgado frito', 5),
                         ('quibe assado', 'salgado assado', 6),
                         ('pizza', 'salgado assado', 9)]
        return self.produtos
