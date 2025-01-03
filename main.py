import os

carros = [
    {"nome": "Chevrolet Tracker", "valor": 120},
    {"nome": "Chevrolet Onix", "valor": 90},
    {"nome": "Chevrolet Spin", "valor": 150},
    {"nome": "Hyundai HB20", "valor": 85},
    {"nome": "Hyundai Tucson", "valor": 120},
    {"nome": "Fiat Uno", "valor": 60},
    {"nome": "Fiat Mobi", "valor": 70},
    {"nome": "Fiat Pulse", "valor": 130}    
]
carros_reservados = []

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def confirmar_acao(mensagem):
    while True:
        resposta = input(mensagem).upper().strip()

        if resposta in ["S", "N"]:
            return resposta
        
        print("OPÇÃO INVÁLIDA! Por favor, insira 'S' para Sim ou 'N' para Não")

def mostrar_carros():
    for index, carro in enumerate(carros):
        print(f"[{index}] - {carro['nome']} - R$ {carro['valor']}/dia")
def alugar_carro():
    limpar_tela()
    print("[Aluguel]\n")
    mostrar_carros()

    reserva = []

    while True:
        try:
            carro_selecionado = int(input("\nQual carro deseja alugar? "))
            if carro_selecionado not in range(len(carros)):
                print("\nOPÇÃO INVÁLIDA! Por favor, insira um opção entre 0 e 7")
            else:
                break
        except ValueError:
            print("\nOPÇÃO INVÁLIDA! Por favor, insira um opção entre 0 e 7")

    while True:
        try:
            qtd_dias_de_reserva = int(input("Por quantos dias desejar alugar o carro? "))
            break
        except ValueError:
            print("\nOPÇÃO INVÁLIDA. Por favor, insira um número inteiro.")

    carro_selecionado = carros[carro_selecionado]
    
    print(f"\nVocê selecionou {carro_selecionado['nome']} por {qtd_dias_de_reserva} dias.")
    print(f"A reserva ficou em R$ {qtd_dias_de_reserva*carro_selecionado['valor']}")

    while True:
            resposta = input("\nDeseja confirmar o aluguel?\n[S]/[N]: ").upper().strip()
            
            if resposta not in ["S", "N"]:
                print("OPÇÃO INVÁLIDA! Por favor, insira 'S' para Sim ou 'N' para Não.")
            else:
                break
    
    if resposta == 'S':
        limpar_tela()

        carros_reservados.append(carro_selecionado)
        carros.remove(carro_selecionado)

        inicializar_locadora()

    else:
        limpar_tela()
        alugar_carro()
def devolver_carro():
    print("[DEVOLUÇÃO]\n")

    if not carros_reservados:
        print("Nenhum carro reservado no momento.")

        while True:
            resposta = input("\nDeseja retornar ao menu principal?\n[S]/[N]: ").upper().strip()
            
            if resposta not in ["S", "N"]:
                print("OPÇÃO INVÁLIDA! Por favor, insira 'S' para Sim ou 'N' para Não.")
            else:
                break       

        if resposta == 'S':
            limpar_tela()
            inicializar_locadora()
        else:
            limpar_tela()
            print("Obrigado por escolher a Locadora Cars by Kelvin")
    
    else:
        for index, carro in enumerate(carros_reservados):
            print(f"[{index}] - {carro['nome']} - R$ {carro['valor']}/dia")

        while True:
            try:
                devolucao_selecionada = int(input("\nQual carro você deseja devolver? "))
                break
            except ValueError:
                print("OPÇÃO INVÁLIDA! Selecione uma devolução válida")

        devolucao_selecionada = carros_reservados[devolucao_selecionada]

        carros.append(devolucao_selecionada)
        carros_reservados.remove(devolucao_selecionada)

        print(f"\nVocê devolveu o carro {devolucao_selecionada['nome']}. Obrigado!")
        
        limpar_tela()

        inicializar_locadora()
def menu_principal():
    print("-"*45)
    print("Bem-Vindo à locadora Cars by Kelvin")
    print("-"*45)
    print()
def sub_menu():
    print()
    print("[0] - Mostrar Carros \n[1] - Alugar Carro \n[2] - Devolver Carro")

    while True:
        try:
            escolha_sub_menu = int(input("\nO que deseja fazer? "))
            if escolha_sub_menu not in range(3):
                print("OPÇÃO INVÁLIDA! Por favor, insira um opção entre 0 e 2")
            else:
                break            
        except ValueError:
            print("OPÇÃO INVÁLIDA! Por favor, insira um número inteiro.")

    if escolha_sub_menu == 0:
        limpar_tela()
        print("[Bem-vindo à Garagem]\n")
        mostrar_carros()

        while True:
            resposta = input("\nDeseja alugar um carro?\n[S]/[N]: ").upper().strip()
            
            if resposta not in ["S", "N"]:
                print("OPÇÃO INVÁLIDA! Por favor, insira 'S' para Sim ou 'N' para Não.")
            else:
                break       

        if resposta == 'S':
            limpar_tela()
            alugar_carro()
        else:
            limpar_tela()
            inicializar_locadora()
    elif escolha_sub_menu == 1:
        limpar_tela()
        alugar_carro()
    else:
        limpar_tela()
        devolver_carro()

def inicializar_locadora():
    menu_principal()
    sub_menu()

inicializar_locadora()