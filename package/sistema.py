class Sistema:
    def __init__(self):
        pass

    def menu_principal(self):
        while True:
            print("\n=== Quiz de Basquete ===")
            print("1. Jogar")
            print("2. Ver ranking")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print("Função 'Jogar' ainda não implementada.")
            elif escolha == "2":
                print("Função 'Ver ranking' ainda não implementada.")
            elif escolha == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
