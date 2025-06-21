import os
import shutil
import sys
from config_V2 import extensoes
from modulo_log_geral import registrar_log_geral
from modulo_log import registrar_log_lixeira, recuperar_origem_arquivo

def obter_categoria(extensao):
    for categoria, lista in extensoes.items():
        if extensao.lower() in lista:
            return categoria
    return "outros"

def categorizar_arquivos(caminho):
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        if os.path.isfile(caminho_completo):
            _, ext = os.path.splitext(arquivo)
            categoria = obter_categoria(ext)
            nova_pasta = os.path.join(caminho, categoria)
            os.makedirs(nova_pasta, exist_ok=True)
            destino = os.path.join(nova_pasta, arquivo)
            shutil.move(caminho_completo, destino)
            print(f"O arquivo {arquivo} foi movido para {destino}")

def criar_arquivos_em_branco(nome, extensao, caminho, quantidade):
    os.makedirs(caminho, exist_ok=True)
    for i in range(1, quantidade + 1):
        nome_completo = f"{nome}_{i}{extensao}"
        caminho_arquivo = os.path.join(caminho, nome_completo)
        with open(caminho_arquivo, "w") as arquivo:
            pass
        print(f"Arquivo {nome_completo} criado em {caminho_arquivo}")
    print(f"\n{quantidade} arquivo(s) criado(s) com sucesso na pasta {caminho}")

def mover_arquivos(nome_arquivo, pasta_antiga, pasta_nova):
    caminho_antigo = os.path.join(pasta_antiga, nome_arquivo)
    if not os.path.exists(caminho_antigo):
        print(f"Arquivo {nome_arquivo} não encontrado em {pasta_antiga}")
        return
    os.makedirs(pasta_nova, exist_ok=True)
    caminho_destino = os.path.join(pasta_nova, nome_arquivo)
    shutil.move(caminho_antigo, caminho_destino)
    print(f"Arquivo {nome_arquivo} movido para {pasta_nova}")

def exibir_arquivos(pasta_escolhida=None):
    if not pasta_escolhida:
        pasta_escolhida = input("Digite uma pasta para exibir os arquivos: ")
    if not os.path.isdir(pasta_escolhida):
        print("Pasta inválida!")
        return

    arquivos = []
    for raiz, dirs, files in os.walk(pasta_escolhida):
        for file in files:
            caminho_completo = os.path.join(raiz, file)
            arquivos.append(caminho_completo)

    opcoes = {
        "1": lambda arqs: sorted(arqs),
        "2": lambda arqs: sorted(arqs, reverse=True),
        "3": lambda arqs: sorted(arqs, key=os.path.getmtime),
        "4": lambda arqs: sorted(arqs, key=os.path.getmtime, reverse=True),
        "5": lambda arqs: sorted(arqs, key=os.path.getsize),
        "6": lambda arqs: sorted(arqs, key=os.path.getsize, reverse=True),
        "7": lambda arqs: [arq for arq in arqs if os.path.splitext(arq)[1] == input("Digite a extensão desejada (ex: .txt): ")]
    }

    nomes_opcoes = {
        "1": "Ordem Alfabética (A - Z)",
        "2": "Ordem Alfabética (Z - A)",
        "3": "Por data (Mais recente primeiro)",
        "4": "Por data (Mais antigo primeiro)",
        "5": "Por tamanho (Menor - Maior)",
        "6": "Por tamanho (Maior - Menor)",
        "7": "Filtrar por extensão"
    }

    for chave, descricao in nomes_opcoes.items():
        print(f"{chave} - {descricao}")

    escolha = input("Escolha a forma de exibição: ")
    if escolha in opcoes:
        arquivos = opcoes[escolha](arquivos)

    for item in arquivos:
        print(item)

def manusear_lixeira():
    caminho_lixeira = "/storage/emulated/0/ArquivosPython/Lixeira_Gerenciador"
    os.makedirs(caminho_lixeira, exist_ok=True)
    arquivos = os.listdir(caminho_lixeira)
    if not arquivos:
        print("A lixeira está vazia.")
    else:
        print("Arquivos na lixeira:")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i}. {arquivo}")

        print("\n1 - Restaurar arquivos")
        print("2 - Excluir permanentemente")
        print("3 - Cancelar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            escolha = input("Digite os números dos arquivos para restaurar (separados por vírgula): ")
            indices = [int(num.strip()) for num in escolha.split(",")]
            for indice in indices:
                nome_arquivo = arquivos[indice - 1]
                caminho_arquivo = os.path.join(caminho_lixeira, nome_arquivo)
                origem = recuperar_origem_arquivo(nome_arquivo)
                shutil.move(caminho_arquivo, origem)
                print(f"{nome_arquivo} restaurado para {origem}")

        elif opcao == "2":
            escolha = input("Digite os números dos arquivos para excluir (separados por vírgula): ")
            indices = [int(num.strip()) for num in escolha.split(",")]
            for indice in indices:
                nome_arquivo = arquivos[indice - 1]
                caminho_arquivo = os.path.join(caminho_lixeira, nome_arquivo)
                os.remove(caminho_arquivo)
                print(f"{nome_arquivo} excluído permanentemente")

        else:
            print("Operação cancelada.")

def renomear_arquivos(pasta_escolhida, nome_novo):
    arquivos = os.listdir(pasta_escolhida)
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i} - {arquivo}")
    escolha = input("Digite o número do arquivo que deseja renomear: ")
    indice = int(escolha) - 1
    nome_antigo = arquivos[indice]
    caminho_antigo = os.path.join(pasta_escolhida, nome_antigo)
    caminho_novo = os.path.join(pasta_escolhida, nome_novo)
    os.rename(caminho_antigo, caminho_novo)
    print(f"{nome_antigo} renomeado para {nome_novo}")

def copiar_arquivo(caminho_arquivo, caminho_copia):
    with open(caminho_arquivo, "rb") as arquivo:
        conteudo = arquivo.read()
    with open(caminho_copia, "wb") as copia:
        copia.write(conteudo)
    print(f"Arquivo copiado para {caminho_copia}")