import os
saldo = 1000

def main():   

    

    def exibir_opcoes():
        os.system('cls')
        print('*****Caixa Eletrônico*****\n')
        print('|||1 - Consultar Saldo')
        print('|||2 - Depositar Saldo')
        print('|||3 - Sacar Saldo')
        print('|||4 - Sair')
        opcao_escolhida = (input('\nEscolha uma opção: \n'))

        if opcao_escolhida == '1':
            consultar_saldo()
        elif opcao_escolhida == '2':
            depositar_saldo()
        elif opcao_escolhida == '3':
            sacar_saldo()
        elif opcao_escolhida == '4':
            finalizar_programa()
        else:
            valor_invalido()
            

    def consultar_saldo():
        os.system('cls')
        print(f'|||Seu saldo atual é de: {saldo}|||')
        input('\nAperte uma tecla para retornar ao menu: ')
        exibir_opcoes()

    def depositar_saldo():
        os.system('cls')
        global saldo
        try:
            print('|||Depositar Valor|||\n')
            valor_depositado = float(input('Qual valor você deseja depositar: '))
            if valor_depositado > 0:
                saldo += valor_depositado
                input('\nVALOR DEPOSITADO - Aperte uma tecla para retornar ao menu: ')  
                exibir_opcoes()
            else:
                valor_invalido()
        except:
            valor_invalido()

    def sacar_saldo():
        os.system('cls')
        global saldo
        try:
            print('|||Sacar Valor|||\n')
            valor_sacado = float(input('Qual valor você deseja sacar: '))
            if valor_sacado > 0:
                saldo -= valor_sacado
                input('\nVALOR SACADO - Aperte uma tecla para retornar ao menu: ')
                exibir_opcoes()
            else:
                valor_invalido()
        except:
            valor_invalido()
        
    def finalizar_programa():
        os.system('cls')
        print('|||Até a próxima!|||')

    def valor_invalido():
        os.system('cls')
        print('Valor invalido!')
        input('Aperte uma tecla para voltar ao menu:')
        exibir_opcoes()


    exibir_opcoes()
    
  
main()