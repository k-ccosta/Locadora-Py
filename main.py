import os

def apresentar_carros():
    os.system("cls" if os.name == "nt" else "clear")

    print("[GARAGEM]\n")

    carros = [
        "Chevrolet Tracker - R$ 120 /dia",
        "Chevrolet Onix - R$ 90 /dia",
        "Chevrolet Spin - R$ 150 /dia",
        "Hyundai HB20 - R$ 85 /dia",
        "Hyundai Tucson - R$ 120 /dia",
        "Fiat Uno - R$ 60 /dia",
        "Fiat Mobi - R$ 70 /dia",
        "Fiat Pulse - R$ 130 /dia"
    ]

    for i, carro in enumerate(carros):
        print(f"[{i}] - {carro}")

    while True:
        resposta = input("\nDeseja alugar um veículo? \n[S]/[N]: ").upper().strip()
            
        if resposta not in ["S", "N"]:
            print("Erro: Por favor, insira 'S' para Sim ou 'N' para Não.")
        else:
            break

    if resposta == "S":
        ... #chamar função de aluguel de carro
    else: 
        os.system("clear")
        iniciar_locadora()

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
        print("[Alugar]")
    else:
        print("[Devolver]")
        
def iniciar_locadora():
    menu_principal()
    submenus()

iniciar_locadora()