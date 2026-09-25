class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria
        self.__disponivel = True

    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Veículo alugado com sucesso.")
        else:
            print("Veículo indisponível.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print("Veículo devolvido com sucesso.")
        else:
            print("O veículo já está disponível.")

    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias

    def esta_disponivel(self):
        return self.__disponivel

    def exibir_informacoes(self):
        disponibilidade = "Sim" if self.__disponivel else "Não"

        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Diária: R$ {self.valor_diaria:.2f}")
        print(f"Disponível: {disponibilidade}")


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, quantidade_portas):
        super().__init__(modelo, placa, valor_diaria)
        self.quantidade_portas = quantidade_portas

    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias

    def exibir_informacoes(self):
        print(f"\nCarro - {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Diária: R$ {self.valor_diaria:.2f}")
        print(f"Portas: {self.quantidade_portas}")

        if self.esta_disponivel():
            print("Disponível: Sim")
        else:
            print("Disponível: Não")


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        valor_total = self.valor_diaria * dias
        desconto = valor_total * 0.10
        return valor_total - desconto

    def exibir_informacoes(self):
        print(f"\nMoto - {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Diária: R$ {self.valor_diaria:.2f}")
        print(f"Cilindradas: {self.cilindradas}")

        if self.esta_disponivel():
            print("Disponível: Sim")
        else:
            print("Disponível: Não")


# Lista onde os objetos serão armazenados
veiculos = []


def cadastrar_veiculo():
    print("\n===== CADASTRO DE VEÍCULO =====")
    print("1 - Carro")
    print("2 - Moto")

    tipo = input("Escolha o tipo de veículo: ")

    if tipo != "1" and tipo != "2":
        print("Opção inválida.")
        return

    modelo = input("Modelo: ")
    placa = input("Placa: ").upper()

    # Verifica se a placa já foi cadastrada
    for veiculo in veiculos:
        if veiculo.placa == placa:
            print("Já existe um veículo cadastrado com essa placa.")
            return

    try:
        valor_diaria = float(input("Valor da diária: R$ "))
    except ValueError:
        print("Valor da diária inválido.")
        return

    if tipo == "1":
        try:
            quantidade_portas = int(input("Quantidade de portas: "))
        except ValueError:
            print("Quantidade de portas inválida.")
            return

        carro = Carro(
            modelo,
            placa,
            valor_diaria,
            quantidade_portas
        )

        veiculos.append(carro)
        print("Carro cadastrado com sucesso.")

    elif tipo == "2":
        try:
            cilindradas = int(input("Cilindradas: "))
        except ValueError:
            print("Cilindrada inválida.")
            return

        moto = Moto(
            modelo,
            placa,
            valor_diaria,
            cilindradas
        )

        veiculos.append(moto)
        print("Moto cadastrada com sucesso.")


def listar_veiculos():
    print("\n===== VEÍCULOS CADASTRADOS =====")

    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
        return

    for veiculo in veiculos:
        veiculo.exibir_informacoes()
        print("-" * 30)


def buscar_veiculo(placa):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            return veiculo

    return None


def alugar_veiculo():
    print("\n===== ALUGUEL DE VEÍCULO =====")

    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
        return

    placa = input("Placa do veículo: ").upper()

    veiculo = buscar_veiculo(placa)

    if veiculo is None:
        print("Veículo não encontrado.")
        return

    if not veiculo.esta_disponivel():
        print("Veículo indisponível.")
        return

    try:
        dias = int(input("Quantidade de dias: "))
    except ValueError:
        print("Quantidade de dias inválida.")
        return

    if dias <= 0:
        print("A quantidade de dias deve ser maior que zero.")
        return

    valor = veiculo.calcular_aluguel(dias)

    print(f"\nVeículo: {veiculo.modelo}")
    print(f"Quantidade de dias: {dias}")
    print(f"Valor do aluguel: R$ {valor:.2f}")

    veiculo.alugar()


def devolver_veiculo():
    print("\n===== DEVOLUÇÃO DE VEÍCULO =====")

    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
        return

    placa = input("Placa do veículo: ").upper()

    veiculo = buscar_veiculo(placa)

    if veiculo is None:
        print("Veículo não encontrado.")
        return

    veiculo.devolver()


def menu():
    while True:
        print("\n===== LOCADORA DE VEÍCULOS =====")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Alugar veículo")
        print("4 - Devolver veículo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_veiculo()

        elif opcao == "2":
            listar_veiculos()

        elif opcao == "3":
            alugar_veiculo()

        elif opcao == "4":
            devolver_veiculo()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")
menu()