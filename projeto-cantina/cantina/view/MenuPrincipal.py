from cantina.view.PaginaInicial import PaginaInicial
from cantina.view.PaginaProdutos import PaginaProdutos
from cantina.view.Menu import Menu
from cantina.services.Pedido import Pedido

class MenuPrincipal:

    def __init__(self, produtos):
        opcao = Menu.__init__(self)

        if opcao == 1:
            opcao = 0
            PaginaInicial.__init__(self,)

        elif opcao == 2:
            PaginaProdutos.listar_produtos(produtos)
            Menu.__init__(self)

        elif opcao == 3:
            Pedido.__init__(self, produtos)
            print(self.pedidos)

        elif opcao == 4:
            login = str(input("Informe o login:"))
            senha = str(input("Informe a senha:"))
            if login == "admin" and senha == "admin":
                opcao_admin = int(input('''
              [1] Gerenciar Conteudo:
              [2] Gerenciar Produtos
              [3] Verificar Pedidos
              Selecione uma opção: '''))

                if opcao_admin == 1:
                    self.conteudo
                    opcao_conteudo = int(input('''Oque você deseja fazer ? 

            [1]Adiconar Conteudo:
            [2]Excluir Conteudo:
            [3]Atualizar Conteudo:

            '''))
                    if opcao_conteudo == 1:
                        self.conteudo.append(input("Adione o conteudo que você desejar:\n"))

                    elif opcao_conteudo == 2:

                        iten_conteudo = int(input("Qual conteudo você deseja excluir ?"))
                        del (self.conteudo[iten_conteudo])

                    elif opcao_conteudo == 3:
                        iten_conteudo2 = int(input("Informe o número do conteudo que você deseja modificar:\n"))

                elif opcao_admin == 2:
                    self.listar_produtos()

                    opcao_2 = int(input('''Oque você deseja fazer ? 
            [1]Adiconar produto
            [2]Excluir produto
            [3]Atualizar produto'''))

                    if opcao_2 == 1:
                        self.produtos.append(input("Adione 1 produto"))
                        self.listar_produtos()

                    elif opcao_2 == 2:
                        iten2 = int(input("Qual produto você deseja excluir ?"))
                        del (produtos[iten2])
                        self.listar_produtos()

                    elif opcao_2 == 3:
                        self.listar_produtos()
                        iten3 = int(input("Informe o número do item você deseja modificar:\n"))
                        indice_produto = int(iten3) - 1
                        produto_temp = produtos[indice_produto]
                        categoria, descricao, valor = list(produto_temp)

                        categoria = input(categoria)
                        descricao = input(descricao)
                        valor = input(str(valor))

                        produtos[indice_produto] = (categoria, descricao, valor)

                elif opcao_admin == 3:
                    self.Verificar_Pedidos()

        elif opcao == 5:
            print('''
            Email: teste@hotmail.com
            Tel: 3333-3333
            Sede: Rua inventado n16,Vitoria(ES'''
                  )

        elif opcao == 6:
            print("Site fechado")

        elif opcao > len(self.rotas) or opcao < 1:
            print('fim do programa')

    def Verificar_Pedidos(self, ):
        if len(self.pedidos) > 0:
            for pedido in self.pedidos:
                print("\n Pedido de: %s,Quantidade pedida: %d, Valor: %d" % (pedido[0], pedido[1], pedido[2]))
                print("Total:", pedido[1] * pedido[2])

        PaginaInicial.__init__(self,)

    def Adicion_Produto(self, produtos):
        produtos.append(input("Adione 1 produto"))
