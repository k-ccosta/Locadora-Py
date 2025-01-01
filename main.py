import os

def carros():
    carros = {
        "Chevrolet Tracker": 120,
        "Chevrolet Onix": 90,
        "Chevrolet Spin": 150,
        "Hyundai HB20": 85,
        "Hyundai Tucson": 120,
        "Fiat Uno": 60,
        "Fiat Mobi": 70,
        "Fiat Pulse": 130
    }

    for index, (chave, valor) in enumerate(carros.items()):
        print(f"[{index}] - {chave} - R$ {valor}/dia")

def apresentar_carros():
    os.system("cls" if os.name == "nt" else "clear")

    print("[GARAGEM]\n")

    carros()

    while True:
        resposta = input("\nDeseja alugar um veículo? \n[S]/[N]: ").upper().strip()
            
        if resposta not in ["S", "N"]:
            print("Erro: Por favor, insira 'S' para Sim ou 'N' para Não.")
        else:
            break

    if resposta == "S":
        ... #chamar função de aluguel de carro
    else: 
        os.system("clear") #ajustar o comando de limpeza de tela
        iniciar_locadora()

def alugar_carro():
    os.system("cls" if os.name == "nt" else "clear")

    print("[Aluguel]\n")

    carros()   

    while True:
        try:
            carro_selecionado = int(input("\nQual carro deseja alugar? "))

            if carro_selecionado in range(8):
                break
            else:
                print("\nOPÇÃO INVÁLIDA! Selecione uma opção entre 0 e 7")                
        except ValueError:
            print("\nOPÇÃO INVÁLIDA! Selecione uma opção entre 0 e 7")

def menu_principal():
    print("-"*45)
    print("Bem-Vindo à locadora Cars by Kelvin")
    print("-"*45)
    print()

def submenus():
    opcoes_submenu = ["Mostrar Carros", "Alugar Carro", "Devolver Carro"]
    
    for i, opcao in enumerate(opcoes_submenu):
        print(f"[{i}] - {opcao}")
    
    # while opcao_submenu_escolhida not in [0, 1, 2]:
    #     try:
    #         opcao_submenu_escolhida = int(input("O que você deseja fazer? "))
    #     except ValueError:
    #         print("\nOPÇÃO INVÁLIDA! Escolha uma opção entre 0 e 3")

    while True:
        try:
            opcao_submenu_escolhida = int(input("\nO que você deseja fazer? "))
            if opcao_submenu_escolhida in range(3):
                break
            else:
                print("OPÇÃO INVÁLIDA! Escolha uma opção entre 0 e 2")                
        except ValueError:
            print("OPÇÃO INVÁLIDA! Escolha uma opção entre 0 e 2")

    if opcao_submenu_escolhida == 0:
        apresentar_carros()
    elif opcao_submenu_escolhida == 1:
        alugar_carro()
    else:
        print("[Devolver]")
        
def iniciar_locadora():
    menu_principal()
    submenus()

iniciar_locadora()