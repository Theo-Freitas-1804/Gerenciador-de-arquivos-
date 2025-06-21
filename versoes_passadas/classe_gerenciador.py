import os
import json
import shutil
from config_V2 import caminhos_padrao, extensoes
from modulo_log_geral import registrar_log_geral, exibir_log
from datetime import datetime
from modulo_log import exibir_log_lixeira, recuperar_origem_arquivo, registrar_log_lixeira
import corretor
import zipfile

class GerenciadorDeArquivos:
    def __init__(self):
        self.caminhos = caminhos_padrao 
        self.extensoes = extensoes 
        self.lixeira_path = os.path.join(self.caminhos["Downloads"], "lixeira")
        self.log_geral_path = os.path.join(self.caminhos["Downloads"], "log_geral.json") 
        self.log_lixeira_path = os.path.join(self.caminhos["Downloads"], "log_lixeira.json") 
        self.ultimos_arquivos_exibidos = [] 
        self.arquivos_marcados_para_excluir = [] 
        self._garantir_estruturas()
        self.entrada_atual = caminhos_padrao.get("padrão", "/storage/emulated/0/Arquivos para testes")

    def _garantir_estruturas(self):
        os.makedirs(self.lixeira_path, exist_ok=True)
        if not os.path.exists(self.log_geral_path):
            with open(self.log_geral_path, "w") as f:
                f.write("[]")
        if not os.path.exists(self.log_lixeira_path):
            with open(self.log_lixeira_path, "w") as f:
                f.write("[]")

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
            escolha = input("Digite os números dos arquivos para restaurar (separados por vírgula): ")
            indices = [int(num.strip()) for num in escolha.split(",")]
            for indice in indices:
                nome_arquivo = arquivos[indice - 1]
                caminho_arquivo = os.path.join(self.lixeira_path, nome_arquivo)
                origem = recuperar_origem_arquivo(nome_arquivo)
                if origem:
                    shutil.move(caminho_arquivo, origem)
                    print(f"{nome_arquivo} restaurado para {origem}")
                    registrar_log_lixeira("restaurado", nome_arquivo, origem)
                else:
                    print(f"Origem não encontrada para {nome_arquivo}. Não foi restaurado.")

        elif opcao == "2":
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
                        print(f"Erro ao excluir {nome_arquivo}: {e}")
        elif opcao == "3":
            print("Saindo")
        else:
            print("Opção inválida.")

    def exibir_arquivos(self, pasta_escolhida=None , filtro_padrao = None):
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

        if not arquivos:
            print("Nenhum arquivo encontrado.")
            return

        opcoes = {
            "1": lambda arqs: sorted(arqs),
            "2": lambda arqs: sorted(arqs, reverse=True),
            "3": lambda arqs: sorted(arqs, key=os.path.getmtime, reverse=True),
            "4": lambda arqs: sorted(arqs, key=os.path.getmtime),
            "5": lambda arqs: sorted(arqs, key=os.path.getsize),
            "6": lambda arqs: sorted(arqs, key=os.path.getsize, reverse=True),
            "7": lambda arqs: [
                arq for arq in arqs
                if os.path.splitext(arq)[1] == input("Digite a extensão desejada (ex: .txt): ")
            ]
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
            self.ultimos_arquivos_exibidos = arquivos
            registrar_log_geral("exibição", f"{len(arquivos)} arquivos exibidos na pasta {pasta_escolhida}")

        for i, item in enumerate(arquivos, start=1):
            print(f"{i} - {item}")

    def renomear_arquivos(self, pasta_escolhida=None, nome_novo=None):
        if not pasta_escolhida:
            pasta_escolhida = input("Digite o caminho ou a pasta onde quer renomear arquivos: ")
        if not os.path.isdir(pasta_escolhida):
            print("Pasta inválida!")
            return

        arquivos = os.listdir(pasta_escolhida)
        if not arquivos:
            print("Nenhum arquivo encontrado.")
            return

        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i} - {arquivo}")
        try:
            escolha = int(input("Digite o número do arquivo que deseja renomear: "))
            if escolha < 1 or escolha > len(arquivos):
                print("Escolha inválida")
                return
            nome_antigo = arquivos[escolha - 1]
            caminho_antigo = os.path.join(pasta_escolhida, nome_antigo)
            if not nome_novo:
                nome_novo = input("Digite o novo nome para o arquivo: ")
            caminho_novo = os.path.join(pasta_escolhida, nome_novo)
            os.rename(caminho_antigo, caminho_novo)
            print(f"{nome_antigo} renomeado para {nome_novo}")
            registrar_log_geral("renomear", f"{nome_antigo} => {nome_novo} em {pasta_escolhida}")
        except ValueError:
            print("Entrada inválida, digite apenas números.")
        except Exception as e:
            print(f"Erro ao renomear: {e}")

    def copiar_arquivos(self, caminho_origem, caminho_copia):
        try:
            with open(caminho_origem, "rb") as arquivo:
                conteudo = arquivo.read()
            with open(caminho_copia, "wb") as copia:
                copia.write(conteudo)
            print(f"Arquivo copiado para {caminho_copia}")
            registrar_log_geral("copiar", f"{caminho_origem} para {caminho_copia}")
        except Exception as e:
            print(f"Erro ao copiar arquivo: {e}")

    def criar_arquivos(self, pasta, quantidade, nome, extensao):
        os.makedirs(pasta, exist_ok=True)
        for i in range(1, quantidade + 1):
            nome_completo = f"{nome}_{i}{extensao}"
            caminho_arquivo = os.path.join(pasta, nome_completo)
            with open(caminho_arquivo, "w") as arquivo:
                pass
            print(f"Arquivo {nome_completo} criado em {caminho_arquivo}")
        registrar_log_geral("criação", f"{quantidade} arquivos criados em {pasta} com nome base {nome} e extensão {extensao}")
        print(f"\n{quantidade} arquivo(s) criado(s) com sucesso na pasta {pasta}")

    def exibir_logs(self):
        def carregar_logs(caminho):
            try:
                with open(caminho, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []

        log_geral = carregar_logs(self.log_geral_path)
        for entrada in log_geral:
            print(json.dumps(entrada, indent=4, ensure_ascii=False))

    def mover_arquivos(self):
     nome_arquivo = input("Digite o nome do arquivo que deseja mover: ")
     pasta_antiga = input("Digite o caminho da pasta de origem: ")
     pasta_nova = input("Digite o caminho da pasta de destino: ")
     caminho_antigo = os.path.join(pasta_antiga, nome_arquivo)
     if not os.path.exists(caminho_antigo):
      print(f"Arquivo '{nome_arquivo}' não encontrado em '{pasta_antiga}'")
      return
     os.makedirs(pasta_nova, exist_ok=True)
     caminho_destino = os.path.join(pasta_nova, nome_arquivo)
     try:
         shutil.move(caminho_antigo, caminho_destino)
         print(f"Arquivo '{nome_arquivo}' movido com sucesso para '{pasta_nova}'")
         registrar_log(f"Arquivo '{nome_arquivo}' movido de '{pasta_antiga}' para '{pasta_nova}'")
     except Exception as e:
          print(f"Erro ao mover o arquivo: {e}")
    
 
    def compactar_arquivos(self):
        self.exibir_arquivos(filtro_padrao="1")
        indices = input("Digite o(s) índice(s):do(s) arquivo(s) que quer compactar: ").split()
        if not hasattr(self, "ultimos_arquivos_exibidos"):
            print("Nenhuma lista disponível")
            return
        selecionados = []
        for i in indices:
            try:
                idx = int(i) - 1
                selecionados.append(self.ultimos_arquivos_exibidos[idx])
            except (ValueError, IndexError):
                print(f"Índice inválido {i}")
        if not selecionados:
            print("Nenhum arquivo válido")
            return
        nome_zip = input("Como quer chamar seu arquivo .zip: ")
        caminho_zip = input("Onde quer salvar seu .ZIP ?")
        if not nome_zip.endswith(".zip"):
            nome_zip += ".zip"
        with ZipFile(nome_zip, "w", compression=ZIP_DEFLATED) as arquivo_zip:
            for caminho in selecionados:
                arquivo_zip.write(caminho, arcname=os.path.basename(caminho))
                print(f"Compactado como {nome_zip}")
                print(f" {nome_zip} compactado em {caminho_zip}")

    def descompactar_arquivos(self, arquivo=None, caminho_destino=None):
        if not arquivo:
            arquivo = input("Digite o nome (com a extensão .zip) do arquivo que quer descompactar: ").strip()
            caminho_origem = input("Onde está o arquivo .ZIP ? (caso não saiba o caminho, pode digitar o final, ex: Música, Download)").strip()
        if not caminho_destino:
            caminho_destino = input("Digite um caminho ou nome padrão (ex: Download): ").strip()

                                                    # Substituir se for caminho padrão (se você estiver usando um dicionário)
        if caminho_destino in caminhos_padrao:
            caminho_destino = caminhos_padrao[caminho_destino]
            print(f"Verificando se o caminho existe: {caminho_destino}")
        if not os.path.exists(caminho_destino):
            print("O caminho informado está incorreto ou não existe. Tente novamente.")
            return False
        caminho_arquivo = os.path.join(caminho_origem, arquivo)
        print(f"Caminho completo do arquivo ZIP: {caminho_arquivo}")
        if not os.path.exists(caminho_arquivo):
            print("Arquivo ZIP não encontrado.")
            return False

        if not zipfile.is_zipfile(caminho_arquivo):
            print("O arquivo informado NÃO é um .zip válido.")
            return False
        try:
            with zipfile.ZipFile(caminho_arquivo, "r") as zip_ref:
                zip_ref.extractall(caminho_destino)
                print(f"✅ Arquivo '{arquivo}' descompactado com sucesso em '{caminho_destino}'.")
                registrar_log_geral(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Arquivo descompactado",
                arquivo = arquivo ,
                caminho_arquivo= caminho_arquivo ,
                caminho_destino = caminho_destino
                )
                return True
        except Exception as e:
            print(f"Erro ao descompactar: {e}")
            return False

    def gerenciar_zip(self):
        print("\n Manusear arquivos zip".center(50))
        opcoes = {
            "1" self.compactar_arquivos ,
            "2":self.descompactar_arquivos
        }       
        for chave , (descricao , _)in opcoes.items:
            print(f"{chave} , {descricao}")
        
       escolha = input("Digite uma opção para aplicar a um .ZIP")
       acao = opcoes.get(escolha)
       if acao:
        acao[1]()
       else:
        print("Opção inválida , tente novamente") 
        
