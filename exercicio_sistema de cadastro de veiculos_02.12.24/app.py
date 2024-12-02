# Sistema de Cadastro de Veículos

# Lista que irá armazenar os veículos cadastrados
veiculos = []

# Função para cadastrar um novo veículo
def cadastrar_veiculo():
    print("\nCadastro de Veículo")
    placa = input("Digite a placa do veículo: ")
    marca = input("Digite o marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")

    veiculo = {
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "ano": ano
    }

    veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso!")

# Função para exibir todos os veículos cadastrados
def criar_veiculo():
    print("\nVeículos Cadastrados:")
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    else:
        for veiculo in veiculos:
            print(f"Modelo: {veiculo['modelo']}, Marca: {veiculo['marca']}, Placa: {veiculo['placa']}, Ano: {veiculo['ano']}")

# Função para editar as informações de um veículo
def editar_veiculo():
    placa = input("\nDigite o modelo do veículo que deseja editar: ")
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            print(f"Editando veículo com a placa: {placa}")
            veiculo['marca'] = input(f"Marca ({veiculo['marca']}): ") or veiculo['marca']
            veiculo['modelo'] = input(f"Modelo ({veiculo['modelo']}): ") or veiculo['modelo']
            veiculo['ano'] = input(f"Ano ({veiculo['Ano']}): ") or veiculo['ano']
            print("Veículo editado com sucesso!")
            return
    print("Veículo não encontrado.")
    
# Função para mostra a lista de veiculos
def lista_veiculo():
    placa = input("\nDigite o modelo do veículo que está disponivél na lista: ")
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            print(f"Editando veículo com a placa: {placa}")
            veiculo['marca'] = input(f"Marca ({veiculo['marca']}): ") or veiculo['marca']
            veiculo['modelo'] = input(f"Modelo ({veiculo['modelo']}): ") or veiculo['modelo']
            veiculo['ano'] = input(f"Ano ({veiculo['Ano']}): ") or veiculo['ano']
            print("Veículo encotrado com sucesso!")
            return
    print("Veículo não encontrado.")

# Função para excluir um veículo
def excluir_veiculo():
    placa = input("\nDigite a placa do veículo que deseja excluir: ")
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            veiculos.remove(veiculo)
            print(f"Veículo com a placa {placa} excluído com sucesso!")
            return
    print("Veículo não encontrado.")

# Função principal para mostrar o menu e chamar as funções apropriadas
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Veículo")
        print("2. Lista de Veículos Cadastrados")
        print("3. Editar Veículo")
        print("4. Excluir Veículo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_veiculo()
        elif opcao == "2":
            lista_veiculo()
        elif opcao == "3":
            editar_veiculo()
        elif opcao == "4":
            excluir_veiculo()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Chama a função do menu
if __name__ == "__main__":
    menu()