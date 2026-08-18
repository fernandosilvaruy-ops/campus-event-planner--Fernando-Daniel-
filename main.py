### menu display ###
def mostrar_menu():
    print("\n=== Planejador de Eventos do Campus ===")
    print("1 - Listar eventos")
    print("2 - Cadastrar novo evento")
    print("3 - Buscar evento pelo nome")
    print("4 - Deletar evento")
    print("5 - Validar data")
    print("6 - Filtrar eventos por categoria")
    print("7 - Marcar evento atendido")
    print("8 - Gerar relatório")
    print("0 - Sair")


### menu chama função ###
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_eventos(eventos)
        elif opcao == "2":
            cadastrar_eventos(eventos)
        elif opcao == "3":
            procurar_eventos(eventos)
        elif opcao == "4":
            deletar_eventos(eventos)
        elif opcao == "5":
            validar_data(eventos)
        elif opcao == "6":
            filtrar_eventos(eventos)
        elif opcao == "7":
            marcar_atendido(eventos)
        elif opcao == "8":
            gerar_relatório(eventos)            
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()