from modelos.carro import Carro

while True:
    validador = input('Quer consultar um veículo? ').lower()

    if validador == 'sim':
        marca= input('Marca do veículo:\n')
        modelo = input('Modelo do veículo:\n')
        ano = int(input('Ano de fabricação:\n'))
        preco = int(input('Preço do veículo:\n'))
        quant = int(input('Quantidade de portas:\n'))

        carro = Carro(marca, modelo, ano, preco, quant)

        print(f'PS: Toda e qualquer visualização/alteração que você fizer AGORA é referente ao veículo de marca {carro.marca} e modelo {carro.modelo}')
        
        while True:

            comando = input('Comando: ').lower()

            if comando == 'relatorio':
                carro.relatorio()

            elif comando == 'alterar preço':
                novoPreco = int(input('Novo preço: '))
                carro.preco = novoPreco

            elif comando == 'informação especifica':
                info = input('Informação: ').lower()
                if info == 'marca':
                    print(f'Marca: {carro.marca}')
                elif info == 'modelo':
                    print(f'Modelo: {carro.modelo}')
                elif info == 'ano':
                    print(f'Ano de fabricação: {carro.anoFabricacao}')
                elif info == 'preço':
                    print(F'Preço: {carro.preco}')
                elif info == 'quantidade de portas':
                    print(f'Quantidade de portas: {carro.quantPortas}')
                else:
                    print('Informação não encontrada')

            elif comando == 'calculo de ipva':
                resultado = carro.calculo_IPVA()
                print(f'IPVA calculado: {resultado}')

            elif comando == 'visualizar outro veiculo':
                carro = None

            elif comando == 'encerrar':
                break

            else:
                print('Comando inválido!')
    else:
        break