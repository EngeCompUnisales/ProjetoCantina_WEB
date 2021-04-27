# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# -*- coding: utf-8 -*-

from cantina.view.PaginaInicial import PaginaInicial
from cantina.view.MenuPrincipal import MenuPrincipal
from cantina.model.Produto import Produto

class Site:

    def __init__(self, ):
        self.produtos = Produto.__init__(self)
        self.pedidos = []

    def pagina_inicial(self, ):
        self.pedidos = PaginaInicial.__init__()
        self.menu()

    def gerenciar_produtos(self, ):
        pass

    def menu(self):
        MenuPrincipal.__init__(self, self.produtos)

s = Site()
s.menu()
