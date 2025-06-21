import os
import json
import shutil
from config_V2 import caminhos_padrao, extensoes
from modulo_log_geral import registrar_log_geral, exibir_log
from datetime import datetime
from modulo_log import exibir_log_lixeira, recuperar_origem_arquivo, registrar_log_lixeira
import corretor
import zipfile

class CentroDeComando:
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
