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

        if isinstance(preco, float) and preco > 0:
            self.__preco = preco
        else:
            raise TypeError('Preço precisa ser um número positivo')

    @abstractmethod
    def __validar_strings(self, string:str): #método interno que valida strings
        if isinstance(string, str):
            return True
        else:
            return False
        
    @abstractmethod
    def __validar_dadosNumericos(self, numero): #método interno que valida números
        if isinstance(numero, int) and numero > 0:
            return True
        else:
            return False

    @abstractmethod
    @property
    def preco(self): #exibe preco de forma simples
        self.__preco

    @abstractmethod
    @preco.setter
    def preco(self, novoPreco): #altera preço, fazendo com que só seja possível alterá-lo através de uma validação interna
        if isinstance(novoPreco, float) and novoPreco > 0:
            self.__preco = novoPreco
        else:
            raise TypeError('Preço precisa ser um número maior que 0')

    @abstractmethod
    def calculo_IPVA(self, preco): #calcula o IPVA com taxa de 4% sob o valor do veículo
        pass

    @abstractmethod
    def relatorio(self): #imprime relatório organizado do veículo
        pass

