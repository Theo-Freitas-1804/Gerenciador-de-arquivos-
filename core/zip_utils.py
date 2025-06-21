import os
import zipfile
from zipfile import ZipFile, ZIP_DEFLATED
from exibicao import exibir_arquivos
from config.config import caminhos_padrao
from logs.modulo_log_geral import registrar_log_geral
from datetime import datetime

# Função para compactar arquivos selecionados
def compactar_arquivos(ultimos_arquivos_exibidos):
    exibir_arquivos(filtro_padrao="1")  # Exibe arquivos na pasta escolhida, com filtro padrão
    indices = input("Digite o(s) índice(s) do(s) arquivo(s) que quer compactar: ").split()
    if not ultimos_arquivos_exibidos:
        print("Nenhuma lista de arquivos disponível.")
        return

    selecionados = []
    for i in indices:
        try:
            idx = int(i) - 1
            selecionados.append(ultimos_arquivos_exibidos[idx])
        except (ValueError, IndexError):  # Verifica se o número é válido
            print(f"Índice inválido: {i}")
    if not selecionados:
        print("Nenhum arquivo válido.")
        return
    nome_zip = input("Como quer chamar seu arquivo .zip: ").strip()
    caminho_zip = input("Onde quer salvar seu .ZIP?: ").strip()

    if not nome_zip.endswith(".zip"):
        nome_zip += ".zip"

    destino_zip = os.path.join(caminho_zip, nome_zip)
    try:
        with ZipFile(destino_zip, "w", compression=ZIP_DEFLATED) as arquivo_zip:
            for caminho in selecionados:
                arquivo_zip.write(caminho, arcname=os.path.basename(caminho))  # Só o nome do arquivo dentro do zip
                print(f"✅ {nome_zip} compactado em {caminho_zip}")
                registrar_log_geral("compactar", f"{nome_zip} criado em {caminho_zip}")
    except Exception as e:
        print(f"Erro ao compactar: {e}")

                                                                                                                                                                                                        # Função para descompactar um arquivo .zip
    # Função para descompactar um arquivo .zip
    def descompactar_arquivos(arquivo=None, caminho_destino=None):
        if not arquivo:
            arquivo = input("Digite o nome do arquivo ZIP: ").strip()
            caminho_origem = input("Caminho onde está o ZIP (ex: Downloads): ").strip()
        else:
            caminho_origem = os.path.dirname(arquivo)
        if not caminho_destino:
            caminho_destino = input("Para onde extrair? (ex: Downloads): ").strip()

                                                    # Verifica se está usando um caminho padrão
        if caminho_destino in caminhos_padrao:
            caminho_destino = caminhos_padrao[caminho_destino]
        if not os.path.exists(caminho_destino):
            print("Caminho inválido.")
            return False

        caminho_arquivo = os.path.join(caminho_origem, arquivo)

        if not os.path.exists(caminho_arquivo):
            print("Arquivo ZIP não encontrado.")
            return False
        if not zipfile.is_zipfile(caminho_arquivo):
            print("O arquivo não é um .zip válido.")
            return False
        try:
            with ZipFile(caminho_arquivo, "r") as zip_ref:
                zip_ref.extractall(caminho_destino)
                print(f"✅ '{arquivo}' descompactado em '{caminho_destino}'.")
                registrar_log_geral(
                "descompactar", f"{arquivo} extraído para {caminho_destino}"                                                               )
            return True
        except Exception as e:
            print(f"Erro ao descompactar: {e}")
            return False

                                                                                                                                                                                                                          # Menu para gerenciar arquivos ZIP
    def gerenciar_zip(ultimos_arquivos_exibidos):
        print("\n📦 Manusear arquivos ZIP".center(50))
        opcoes = {
        "1": ("Compactar arquivos", lambda: compactar_arquivos(ultimos_arquivos_exibidos)),
        "2": ("Descompactar arquivos", descompactar_arquivos)
        }
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave} - {descricao}")

        escolha = input("Digite uma opção para aplicar a um .ZIP: ").strip()
        acao = opcoes.get(escolha)
        if acao:
            acao[1]()  # Executa a função associada à opção
        else:
            print("❌ Opção inválida.")              
