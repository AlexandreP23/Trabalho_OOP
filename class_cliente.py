
class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone

    
    def imprimir_cliente(self):
        return f"Cliente: {self.__nome}, CPF: {self.__cpf}, Endereço: {self.__endereco}, Telefone: {self.__telefone}"

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

class Premium(Cliente):
    def __init__(self, nome, cpf, endereco, telefone, limite):
        super().__init__(nome, cpf, endereco, telefone)
        self.__limite = limite

    
    def imprimir_cliente(self):
        return f"Cliente Premium: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}, Telefone: {self.telefone}, Limite: {self.__limite}"

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite


cliente_1 = Premium("Alex", "8273827-38", "Rua das Filhas, 121", "99993829", "Sem limite")
cliente_1.nome = "Rodrigo"

cliente_2 = Cliente("João", "9384938-49", "Rua dos Migué, 171", "9998988938")
cliente_2.nome = "Marcelo"


print(cliente_2.imprimir_cliente())

print(cliente_1.imprimir_cliente())
