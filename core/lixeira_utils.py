import os
import shutil
from logs.log_lixeira import recuperar_origem_arquivo, registrar_log_lixeira
from exibicao import exibir_arquivos

class LixeiraManager:
    def __init__(self, lixeira_path):
        self.lixeira_path = lixeira_path

    def listar_lixeira(self):
        arquivos = os.listdir(self.lixeira_path)
        if not arquivos:
            print("A lixeira está vazia.")
            return

        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i} - {arquivo}")
            print("\n1) Restaurar arquivos")
            print("2) Excluir permanentemente")
            print("3) Cancelar")
            opcao = input("Digite uma opção: ")

            if opcao == "1":
                 self..restaurar_arquivos(arquivos)

            elif opcao == "2":
                self._excluir_permanentemente(arquivos)

            elif opcao == "3":
                print("Saindo")
                break
            else:
                print("Opção inválida.")

    def restaurar_arquivos(self, arquivos):
        escolha = input("Digite os números dos arquivos para restaurar (separados por vírgula): ")
        indices = [int(num.strip()) for num in escolha.split(",")]
        for indice in indices:
            nome_arquivo = arquivos[indice - 1]
            caminho_arquivo = os.path.join(self.lixeira_path, nome_arquivo)
            origem = recuperar_origem_arquivo(nome_arquivo)
            if origem:
                try:
                    shutil.move(caminho_arquivo, origem)
                    print(f"{nome_arquivo} restaurado para {origem}")
                     registrar_log_lixeira("restaurado", nome_arquivo, origem)
            
                except FileNotFoundError:
                    
                    print("Arquivo não encontrado , impossível mover")
            else:
                print(f"Origem não encontrada para {nome_arquivo}. Não foi restaurado.")

    def excluir_permanentemente(self, arquivos):
        exibir_arquivos()
        escolha = input("Digite os números dos arquivos para excluir (separados por vírgula): ")
        indices = [int(num.strip()) for num in escolha.split(",")]
        for indice in indices:
            if 1 <= indice <= len(arquivos):
                nome_arquivo = arquivos[indice - 1]
                caminho_arquivo = os.path.join(self.lixeira_path, nome_arquivo)
                try:
                    os.remove(caminho_arquivo)
                    print(f"{nome_arquivo} excluído permanentemente")
                    registrar_log_lixeira("excluído permanentemente", nome_arquivo)
                except Exception as e:
                    print(f"Erro ao excluir {nome_arquivo}: {e}")")")"))
