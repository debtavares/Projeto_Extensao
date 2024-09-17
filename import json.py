import json
import os

# Caminhos dos arquivos
CAMINHO_EVENTOS = 'eventos.json'
CAMINHO_PARTICIPANTES = 'participantes.json'
CAMINHO_RELACIONAMENTOS = 'relacionamentos.json'

# Listas para armazenar os dados
eventos = []
participantes = []
relacionamentos = []

# Funções para carregar dados de arquivos JSON
def carregar_dados():
    global eventos, participantes, relacionamentos
    if os.path.exists(CAMINHO_EVENTOS):
        with open(CAMINHO_EVENTOS, 'r') as f:
            eventos = json.load(f)
    else:
        eventos = []

    if os.path.exists(CAMINHO_PARTICIPANTES):
        with open(CAMINHO_PARTICIPANTES, 'r') as f:
            participantes = json.load(f)
    else:
        participantes = []

    if os.path.exists(CAMINHO_RELACIONAMENTOS):
        with open(CAMINHO_RELACIONAMENTOS, 'r') as f:
            relacionamentos = json.load(f)
    else:
        relacionamentos = []

# Funções para salvar dados em arquivos JSON
def salvar_dados():
    with open(CAMINHO_EVENTOS, 'w') as f:
        json.dump(eventos, f, indent=4)
    with open(CAMINHO_PARTICIPANTES, 'w') as f:
        json.dump(participantes, f, indent=4)
    with open(CAMINHO_RELACIONAMENTOS, 'w') as f:
        json.dump(relacionamentos, f, indent=4)

def adicionar_evento():
    nome = input("Digite o nome do evento: ")
    data = input("Digite a data do evento (AAAA-MM-DD): ")
    descricao = input("Digite a descrição do evento: ")
    evento = {'nome': nome, 'data': data, 'descricao': descricao}
    eventos.append(evento)
    salvar_dados()
    print(f"Evento '{nome}' adicionado com sucesso!")

def listar_eventos():
    if eventos:
        print("\nEventos:")
        for evento in eventos:
            print(f"Nome: {evento['nome']}, Data: {evento['data']}, Descrição: {evento['descricao']}")
    else:
        print("Nenhum evento encontrado.")

def adicionar_participante():
    nome = input("Digite o nome do participante: ")
    idade = input("Digite a idade do participante: ")
    email = input("Digite o e-mail do participante: ")
    participante = {'nome': nome, 'idade': idade, 'email': email}
    participantes.append(participante)
    salvar_dados()
    print(f"Participante '{nome}' adicionado com sucesso!")

def listar_participantes():
    if participantes:
        print("\nParticipantes:")
        for participante in participantes:
            print(f"Nome: {participante['nome']}, Idade: {participante['idade']}, E-mail: {participante['email']}")
    else:
        print("Nenhum participante encontrado.")

def associar_participante_evento():
    nome_evento = input("Digite o nome do evento ao qual o participante será associado: ")
    nome_participante = input("Digite o nome do participante a ser associado: ")
    
    evento = next((e for e in eventos if e['nome'] == nome_evento), None)
    participante = next((p for p in participantes if p['nome'] == nome_participante), None)
    
    if evento and participante:
        relacionamento = {'evento': nome_evento, 'participante': nome_participante}
        relacionamentos.append(relacionamento)
        salvar_dados()
        print(f"Participante '{nome_participante}' associado ao evento '{nome_evento}' com sucesso!")
    else:
        print("Evento ou participante não encontrado.")

def listar_participantes_por_evento():
    nome_evento = input("Digite o nome do evento para listar os participantes associados: ")
    participantes_associados = [p for p in relacionamentos if p['evento'] == nome_evento]
    if participantes_associados:
        print(f"\nParticipantes associados ao evento '{nome_evento}':")
        for assoc in participantes_associados:
            participante = next(p for p in participantes if p['nome'] == assoc['participante'])
            print(f"- Nome: {participante['nome']}, Idade: {participante['idade']}, E-mail: {participante['email']}")
    else:
        print(f"Nenhum participante associado ao evento '{nome_evento}'.")

def deletar_evento():
    nome_evento = input("Digite o nome do evento que deseja deletar: ")
    global eventos, relacionamentos
    eventos = [e for e in eventos if e['nome'] != nome_evento]
    relacionamentos = [r for r in relacionamentos if r['evento'] != nome_evento]
    salvar_dados()
    print(f"Evento '{nome_evento}' deletado com sucesso!")

def deletar_participante():
    nome_participante = input("Digite o nome do participante que deseja deletar: ")
    global participantes, relacionamentos
    participantes = [p for p in participantes if p['nome'] != nome_participante]
    relacionamentos = [r for r in relacionamentos if r['participante'] != nome_participante]
    salvar_dados()
    print(f"Participante '{nome_participante}' deletado com sucesso!")

def menu():
    carregar_dados()
    while True:
        print("\n--- Menu de Gerenciamento de Eventos e Participantes ---")
        print("1. Adicionar Evento")
        print("2. Listar Eventos")
        print("3. Adicionar Participante")
        print("4. Listar Participantes")
        print("5. Associar Participante a Evento")
        print("6. Listar Participantes por Evento")
        print("7. Deletar Evento")
        print("8. Deletar Participante")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_evento()
        elif escolha == '2':
            listar_eventos()
        elif escolha == '3':
            adicionar_participante()
        elif escolha == '4':
            listar_participantes()
        elif escolha == '5':
            associar_participante_evento()
        elif escolha == '6':
            listar_participantes_por_evento()
        elif escolha == '7':
            deletar_evento()
        elif escolha == '8':
            deletar_participante()
        elif escolha == '9':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
menu()
