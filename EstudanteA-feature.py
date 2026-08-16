
# local de testes de funções

eventos = [
    ["hackatlon", "25/12", "IFB Riacho Fundo", "Tecnologia"]
]

# Funçao responsavel por listar os eventos.
def listar_eventos(eventos):
    print("\n--- Lista de eventos ---")
    for evento in eventos:
        print(f"Nome: {evento[0]} | Data: {evento[1]} | Local: {evento[2]} | Tema: {evento[3]}")

listar_eventos(eventos)