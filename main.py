import re
# local de testes de funções

eventos = []


# Funçao responsavel por listar os eventos.
def listar_eventos(eventos):
    print("\n--- Lista de eventos ---")
    for evento in eventos:
        print(f"Nome: {evento["nome"]} | Data: {evento["data"]} | Local: {evento["local"]} | Categoria: {evento["categoria"]}")

# Função responsável por cadastrar um evento.
def cadastrar_eventos(eventos, nome, data, local, categoria):
    eventoBase = {
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }

    eventos.append(eventoBase)
    print(f"\nEvento '{nome}' cadastrado com sucesso!")

#Função para procurar evento por nome. 
def procurar_eventos(eventos, nome):
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            print(f"\nEvento encontrado: Nome: {evento["nome"]} | Data: {evento["data"]} | Local: {evento["local"]} | Categoria: {evento["categoria"]}")
            return evento
    print(f"\nEvento '{nome}' não encontrado.")
    return None

#função para remover evento por nome
def remover_evento(eventos, nome):
    print("Removendo o evento :", nome)
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            eventos.remove(evento)
            print(f"\nEvento '{nome}' removido com sucesso!")
            return
    print(f"\nEvento '{nome}' não encontrado para remoção.")

#função para validar data no formato dd/mm


def validar_data(data):
    padrao = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    return bool(re.match(padrao, data))
    

#### Função filtrar eventos por categoria      
def buscar_evento_categoria():
    categoria_usuario = input("Digite a categoria: ")

    for evento in eventobase:                      ### Definir nomes ###
        if evento["categoria"] == categoria_usuario: ### Definir nomes ###
         print(evento["nome"])                    ### Definir nomes ###


### Função marcar presença
def marcarEventoAtendido():
    listar_eventos(eventos)

    id_escolhido = int(input("Digite o ID do Evento comparecido: "))

    for evento in eventos:
        if evento["id"] == id_escolhido:
            evento["atendido"] = True


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

def leituraDadoEvento():    
    nome = input("Entre com o nome do evento: ")
    data = input("Entre com a data do evento: ")
    while (validar_data(data) == False):
        data = input("Entre com a data do evento: ")
    local = input("Entre com o local do evento: ")
    categoria = input("Entre com a categoria do evento: ")
    print("Leitura de dados realizada com sucesso!")
    return nome, data, local, categoria

### menu chama função ###
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_eventos(eventos)
        elif opcao == "2":
            #cadastrar evento
            nome, data, local, categoria = leituraDadoEvento()
            cadastrar_eventos(eventos, nome, data, local, categoria)
        elif opcao == "3":
            nome = input("Digite  o nome do evento: ")
            procurar_eventos(eventos, nome)
        elif opcao == "4":
            nome = input("digite o nome do evento a ser removido: ")
            remover_evento(eventos, nome)
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