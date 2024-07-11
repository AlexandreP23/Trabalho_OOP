import csv

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

def salvar_cliente_csv(cliente):
    with open('clientes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if isinstance(cliente, Premium):
            writer.writerow([cliente.nome, cliente.cpf, cliente.endereco, cliente.telefone, cliente.limite])
        else:
            writer.writerow([cliente.nome, cliente.cpf, cliente.endereco, cliente.telefone, ''])

def listar_clientes_csv():
    try:
        with open('clientes.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[4]:  # Verifica se há um limite, ou seja, se é um cliente Premium
                    print(f"Cliente Premium: Nome: {row[0]}, CPF: {row[1]}, Endereço: {row[2]}, Telefone: {row[3]}, Limite: {row[4]}")
                else:
                    print(f"Cliente: Nome: {row[0]}, CPF: {row[1]}, Endereço: {row[2]}, Telefone: {row[3]}")
    except FileNotFoundError:
        print("Nenhum cliente cadastrado.")

def menu():
    while True:
        print("\n1. Cadastrar Cliente")
        print("2. Consultar Clientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            tipo_cliente = input("Cliente Premium? (s/n): ")

            if tipo_cliente.lower() == 's':
                limite = input("Limite: ")
                cliente = Premium(nome, cpf, endereco, telefone, limite)
            else:
                cliente = Cliente(nome, cpf, endereco, telefone)
            
            salvar_cliente_csv(cliente)
            print("Cliente cadastrado com sucesso!")

        elif opcao == '2':
            listar_clientes_csv()

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
