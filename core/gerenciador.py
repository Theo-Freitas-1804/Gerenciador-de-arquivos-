# core/gerenciador.py

import os
import shutil
from logs.log_geral import registrar_log_geral

class FuncoesGeraiss:
    def renomear_arquivos(self, pasta, nome_novo=None):
        if not os.path.isdir(pasta):
            print("Pasta inválida!")
            return
        arquivos = os.listdir(pasta)
        if not arquivos:
            print("Nenhum arquivo encontrado.")
            return
        for i, arquivo in enumerate(arquivos, 1):
            print(f"{i} - {arquivo}")

        try:
            escolha = int(input("Digite o número do arquivo que deseja renomear: "))
            if not (1 <= escolha <= len(arquivos)):
                print("Escolha inválida.")
                return
            nome_antigo = arquivos[escolha - 1]
            caminho_antigo = os.path.join(pasta, nome_antigo)

            if not nome_novo:
                nome_novo = input("Digite o novo nome: ")
                caminho_novo = os.path.join(pasta, nome_novo)
                os.rename(caminho_antigo, caminho_novo)
                print(f"{nome_antigo} renomeado para {nome_novo}")
                registrar_log_geral("renomear", f"{nome_antigo} => {nome_novo} em {pasta}")
        except ValueError:
            print("Entrada inválida. Use apenas números.")
        except Exception as e:
            print(f"Erro ao renomear: {e}")

    def copiar_arquivos(self, origem, destino):
        try:
            with open(origem, "rb") as arquivo:
                conteudo = arquivo.read()
            with open(destino, "wb") as copia:
                copia.write(conteudo)
            print(f"Arquivo copiado para {destino}")
            registrar_log_geral("copiar", f"{origem} => {destino}")

        except Exception as e:
            print(f"Erro ao copiar arquivo: {e}")

    def criar_arquivos(self, pasta, quantidade, nome, extensao):
        os.makedirs(pasta, exist_ok=True)
        for i in range(1, quantidade + 1):
            nome_completo = f"{nome}_{i}{extensao}"
            caminho = os.path.join(pasta, nome_completo)
            with open(caminho, "w"):
                pass
            print(f"{nome_completo} criado em {pasta}")
            registrar_log_geral("criação", f"{quantidade} arquivos em {pasta} como {nome}_{extensao}")

    def mover_arquivos(self, nome_arquivo, origem, destino):
        caminho_origem = os.path.join(origem, nome_arquivo)
        caminho_destino = os.path.join(destino, nome_arquivo)
        if not os.path.exists(caminho_origem):
            print(f"Arquivo '{nome_arquivo}' não encontrado em '{origem}'")
            return
        os.makedirs(destino, exist_ok=True)
        try:
            shutil.move(caminho_origem, caminho_destino)
            print(f"{nome_arquivo} movido de {origem} para {destino}")
            registrar_log_geral("mover", f"{nome_arquivo}: {origem} => {destino}")
        except Exception as e:
            print(f"Erro ao mover o arquivo: {e}")
