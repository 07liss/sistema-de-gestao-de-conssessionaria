from modelos.veiculo import Veiculo

class Carro(Veiculo):

    def calculo_IPVA(self):
        ipva = self.preco * 0.04
        return ipva