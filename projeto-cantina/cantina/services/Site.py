# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# -*- coding: utf-8 -*-

class Site:

    def __init__(self, ):
        self.opcao = 1
        self.conteudo = [['Bem Vindo', 'Fique por dentro das novidades da loja'],
                         ['O gerente ficou maluco', 'Todos o setor de salgados e frituras está pela metade do preço']]
        self.produtos = [('pastel de frango', 'salgado frito', 7),  # (descricao, categoria, valor)
                         ('coxinha', 'salgado frito', 5),
                         ('quibe assado', 'salgado assado', 6),
                         ('pizza', 'salgado assado', 9)]
        self.pedidos = []

        # self.usuarios = [(admin,admin)]

    def pagina_inicial(self, ):
        for c in self.conteudo:
            print(c)
        self.pedidos.append([self.produtos[1], 3])
        self.menu_principal()

    def pagina_produtos(self, ):
        for c in self.produtos:
            print(c)
        self.menu_principal()

        self.pedidos.append([self.produtos[0], 2])

    def gerenciar_produtos(self, ):
        pass

    def fazer_pedido(self, ):
        nome = str(input("Oque você gostaria de pedir ?"))
        quant = int(input("Quantos"))
        # p = (produto, categoria, valor)
        for produto in self.produtos:
            if produto[0] == nome:
                self.pedidos.append([produto[0], quant, produto[2]])
                print("Pedido realizado.")
                break

        self.menu_principal()

    def Verificar_Pedidos(self, ):
        if len(self.pedidos) > 0:
            for pedido in self.pedidos:
                print("\n Pedido de: %s,Quantidade pedida: %d, Valor: %d" % (pedido[0], pedido[1], pedido[2]))
                print("Total:", pedido[1] * pedido[2])

        self.menu_principal()

    def Adicion_Produto(self, ):
        self.produtos.append(input("Adione 1 produto"))

    def listar_produtos(self, ):
        for p in enumerate(self.produtos):
            print("[%d] Categoria: %s Produto: %s Preço: %d" % (p[0] + 1, p[1][0], p[1][1], p[1][2]))

    # def listar_conteudo(self,):
    # for cont in enumerate(self.conteudo):
    #  print("[%d] Conteudo:" % (cont[0] + 1, cont[1][0]))

    def menu_principal(self, ):
        print("\n\n")
        self.rotas = ['Página Inicial', 'Produtos', 'Fazer Pedido', 'Administração', 'Contato', 'Sair']
        for r in enumerate(self.rotas):
            print("[%d] %s" % (r[0] + 1, r[1]))
        opcao = int(input("digite sua escolha: "))
        if opcao == 1:
            self.pagina_inicial()
        elif opcao == 2:
            self.listar_produtos()
            self.pagina_produtos()

        elif opcao == 3:
            self.fazer_pedido()
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
                        del (self.produtos[iten2])
                        self.listar_produtos()

                    elif opcao_2 == 3:
                        self.listar_produtos()
                        iten3 = int(input("Informe o número do item você deseja modificar:\n"))
                        indice_produto = int(iten3) - 1
                        produto_temp = self.produtos[indice_produto]
                        categoria, descricao, valor = list(produto_temp)

                        categoria = input(categoria)
                        descricao = input(descricao)
                        valor = input(str(valor))

                        self.produtos[indice_produto] = (categoria, descricao, valor)

                elif opcao_admin == 3:
                    self.Verificar_Pedidos()

                # while:
        # print("Login ou Senha incorretos")

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

    def menu(self, ):
        print('''
  [1]Pagina Inicial
  [2]Produtos
  [3]Fazer Pedido
  [4]Contato
  [5]Administracao
  ''')
        opcao = int(input("digite sua escolha: "))


# menu()
s = Site()
s.menu_principal()

