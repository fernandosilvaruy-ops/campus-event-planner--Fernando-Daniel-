
# local de testes de funções

#valores da variavel só representativos para teste da função listar_eventos
eventos = [
    ["hackatlon", "25/12", "IFB Riacho Fundo", "Tecnologia"]
]

# Funçao responsavel por listar os eventos.
def listar_eventos(eventos):
    print("\n--- Lista de eventos ---")
    for evento in eventos:
        print(f"Nome: {evento[0]} | Data: {evento[1]} | Local: {evento[2]} | Tema: {evento[3]}")

listar_eventos(eventos)

# Função responsável por cadastrar um evento.
def cadastrar_evento(eventos, nome, data, local, tema):
    evento = [nome, data, local, tema]
    eventos.append(evento)
    print(f"\nEvento '{nome}' cadastrado com sucesso!")

#Função para procurar evento por nome. 
def procurar_evento(eventos, nome):
    for evento in eventos:
        if evento[0].lower() == nome.lower():
            print(f"\nEvento encontrado: Nome: {evento[0]} | Data: {evento[1]} | Local: {evento[2]} | Tema: {evento[3]}")
            return evento
    print(f"\nEvento '{nome}' não encontrado.")
    return None

#função para remover evento por nome
def remover_evento(eventos, nome):
    for evento in eventos:
        if evento[0].lower() == nome.lower():
            eventos.remove(evento)
            print(f"\nEvento '{nome}' removido com sucesso!")
            return
    print(f"\nEvento '{nome}' não encontrado para remoção.")

#função para validar data no formato dd/mm
def validar_data(data):
    import re
    padrao = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])$"
    if re.match(padrao, data):
        return True
    else:
        print("\nData inválida. Use o formato dd/mm.")
        return False
    


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