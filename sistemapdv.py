jogos = []
precoFabrica = []
precoLoja = []
estoqueDisponivel = []
vendas = []
compras = []

user = 'Administrador'
key = 'adminadmin'
login1 = True
menu = '0'
saldo = 500.00
lucroTotal = 0.00
lucro = 12

while login1:

    # LOGIN DE USUARIO
    print('\n----------------------  LOGIN DE USUÁRIO  ----------------------')
    usuario = input('LOGIN: ')
    senha = input('SENHA: ')

    # VALIDAÇAO LOGIN
    if usuario == user and senha == key:
        login2 = True
        while login2:
            menu1 = '1'
            menu2 = '1'
            menu3 = '1'
            menu4 = '1'
            menu5 = '1'

            # MENU PRINCIPAL
            menu = input(f'\n---------------------   GAMES PLAY STORE   ---------------------\n'
                         f'SALDO DO CAIXA: {saldo:.2f}\n'
                         f'MARGEM DE LUCRO: {lucro}%\n'
                         '\n(1) REGISTRAR VENDA\n'
                         '(2) COMPRAR ESTOQUE\n'
                         '(3) RESUMO GERAL DA LOJA\n'
                         '(4) CADASTRAR JOGO NA FÁBRICA\n'
                         '(5) ALTERAR MARGEM DE LUCRO\n'
                         '(0) SAIR\n')

            # REGISTRAR VENDA
            if menu == '1':
                while menu1 == '1':
                    print(
                        '\n-------------------   CATALOGO DA LOJA   -----------------------\n'
                        f'\nSALDO DO CAIXA: {saldo:.2f}\n'
                        '\nID    NOME DO JOGO             ESTOQUE DA LOJA    PREÇO DE VENDA\n')
                    for idJogos in range(len(jogos)):
                        idJog = str(idJogos)
                        print(
                            f'{idJog.ljust(6)}{jogos[idJogos].ljust(25)}{str(estoqueDisponivel[idJogos]).ljust(19)}{precoLoja[idJogos]:.2f}\n')

                    vendasJogos = int(input('\n-------------------   VENDA PARA CLIENTES   --------------------'
                                            '\nID do jogo: '))
                    quantidadeVendas = int(input('QUANTIDADE: '))

                    if estoqueDisponivel[vendasJogos] >= quantidadeVendas:
                        saldo += (precoLoja[vendasJogos] * quantidadeVendas)
                        lucroTotal += ((precoLoja[vendasJogos] - precoFabrica[vendasJogos]) * quantidadeVendas)
                        estoqueDisponivel[vendasJogos] -= quantidadeVendas
                        vendas[vendasJogos] += quantidadeVendas
                        print(f'{jogos[vendasJogos]} foi vendido com SUCESSO!')

                    else:
                        print('A quantidade deste jogo em estoque é INSUFICIENTE!')
                    menu1 = input('\n(1) VENDER OUTRO JOGO'
                                  '\n(0) SAIR\n')

            # COMPRAR ESTOQUE
            elif menu == '2':
                while menu2 == '1':
                    print(
                        '\n-------------------  CATALOGO DA FABRICA  ----------------------\n'
                        f'\nSALDO DO CAIXA: {saldo:.2f}\n'
                        f'\nID    NOME DO JOGO             PEÇO DE CUSTO    ESTOQUE DA LOJA    PREÇO DE REVENDA (+{lucro}%)\n')
                    for idJogos in range(len(jogos)):
                        idJog = str(idJogos)
                        print(
                            f'{idJog.ljust(6)}{jogos[idJogos].ljust(25)}{precoFabrica[idJogos]:.2f}{str(estoqueDisponivel[idJogos]).center(33)}{precoLoja[idJogos]:.2f}\n')

                    comprarJogos = int(input(
                        '\n---------------------  COMPRAR PARA LOJA  ----------------------'
                        '\nID do jogo: '))
                    quantidadeCompra = int(input('QUANTIDADE: '))

                    if precoFabrica[comprarJogos] * quantidadeCompra < saldo:
                        saldo -= (precoFabrica[comprarJogos] * quantidadeCompra)
                        estoqueDisponivel[comprarJogos] += quantidadeCompra
                        compras[comprarJogos] += quantidadeCompra
                        print(f'{jogos[comprarJogos]} foi compro com SUCESSO!')

                    else:
                        print('Saldo INSUFICIENTE!')
                    menu2 = input('\n(1) COMPRAR OUTRO JOGO'
                                  '\n(0) SAIR\n')

            # RESUMO GERAL DA LOJA
            elif menu == '3':
                comprasTotal = sum(compras)
                vendasTotal = sum(vendas)
                print(
                    '\n-------------------  RESUMO GERAL DA LOJA  ---------------------\n'
                    '\nNOME DA LOJA: GAMES PLAY STORE'
                    f'\nGERENTE: {user}'
                    f'\nSALDO DO CAIXA: R$ {saldo:.2f}'
                    f'\nMARGEM DE LUCRO: {lucro}%'
                    f'\nLUCRO TOTAL: R$ {lucroTotal:.2f}'
                    f'\nACERVO DE JOGOS: {len(jogos)} UNIDADES'
                    f'\nTOTAL DE COMPRAS: {comprasTotal} UNIDADES'
                    f'\nTOTAL DE VENDAS: {vendasTotal} UNIDADES\n'
                    f'\nID    NOME DO JOGO             ESTOQUE DA LOJA    COMPRAS    VENDAS\n')
                for idJogos in range(len(jogos)):
                    idJog = str(idJogos)
                    print(
                        f'{idJog.ljust(6)}{jogos[idJogos].ljust(25)}{str(estoqueDisponivel[idJogos]).ljust(19)}{str(compras[idJogos]).ljust(11)}{str(vendas[idJogos]).ljust(10)}\n')

                menu3 = input('\nCLIQUE PARA SAIR\n')

            # CADASTRAR JOGO NA FÁBRICA
            elif menu == '4':
                while menu4 == '1':
                    cadastroJogos = input('\n----------------   CADASTRAR JOGO NA FÁBRICA   -----------------'
                                          '\nInsira o NOME do jogo: ')
                    cadastroPrecoCusto = float(input('Digite o preço de CUSTO: '))
                    print(f'{cadastroJogos} foi cadastrado com SUCESSO!')

                    jogos.append(cadastroJogos)
                    precoFabrica.append(cadastroPrecoCusto)
                    precoLoja.append(cadastroPrecoCusto * ((lucro / 100) + 1))
                    estoqueDisponivel.append(0)
                    vendas.append(0)
                    compras.append(0)

                    menu4 = input('\n(1) CADASTRAR OUTRO'
                                  '\n(0) SAIR\n')

            # ALTERAR PORCENTAGEM DE LUCRO
            elif menu == '5':
                while menu5 == '1':
                    novoLucro = int(input('\n----------------   ALTERAR MARGEM DE LUCRO   -------------------\n'
                                          'Digite a NOVA porcentagem: '))
                    if novoLucro >= 0:
                        lucro = novoLucro
                        print(f'A MARGEM DE LUCRO foi ajustada para {lucro}%')

                    else:
                        print('Porcentagem INVALIDA!')
                    menu5 = input('\n(1) REAJUSTAR MARGEM DE LUCRO'
                                  '\n(0) SAIR\n')

            # SAIR
            elif menu == '0':
                login2 = False
    else:
        print('Usuário ou senha INVÁLIDOS!\n'
              '----------------------------------------------------------------\n')
