
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