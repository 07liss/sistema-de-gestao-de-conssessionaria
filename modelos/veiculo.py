from abc import ABC, abstractmethod;

class Veiculo(ABC):
    def __init__(self, marca:str, modelo:str, anoFabricacao:int, preco:float, quantidadePortas:int): #recebe os dados
        if self.__validar_strings(marca) and self.__validar_strings(modelo):
            self.__marca = marca
            self.__modelo = modelo
        else:
            raise TypeError('Marca e modelo precisam ser textos')

        if self.__validar_dadosNumericos(quantidadePortas) and self.__validar_dadosNumericos(anoFabricacao):
            self.__quantPortas = quantidadePortas
            self.__anoFabricacao = anoFabricacao
        else:
            raise TypeError('Quantidade de portas e ano de fabricação precisam ser inteiros positivos')

        if isinstance(preco, (int, float)) and preco > 0:
            self.__preco = preco
        else:
            raise TypeError('Preço precisa ser um número positivo')

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def anoFabricacao(self):
        return self.__anoFabricacao

    @property
    def preco(self): #exibe preco de forma simples
        return self.__preco

    @property
    def quantPortas(self):
        return self.__quantPortas

    def __validar_strings(self, string:str): #método interno que valida strings
        if isinstance(string, str):
            return True
        else:
            return False
        
    def __validar_dadosNumericos(self, numero): #método interno que valida números
        if isinstance(numero, int) and numero > 0:
            return True
        else:
            return False

    @preco.setter
    def preco(self, novoPreco): #altera preço, fazendo com que só seja possível alterá-lo através de uma validação interna
        if isinstance(novoPreco, (float, int)) and novoPreco > 0:
            self.__preco = novoPreco
            print('Preço alterado')

    @abstractmethod
    def calculo_IPVA(self, preco): #calcula o IPVA com taxa de 4% sob o valor do veículo
        pass

    def relatorio(self): #imprime relatório organizado do veículo
        print('='*10, 'RELATÓRIO', '='*10)
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno de Fabricação: {self.anoFabricacao}\nPreço: {self.preco}\nQuantidade de Portas: {self.quantPortas}')

