import json
from datetime import datetime
import os

def registrar_log_geral(data , acao , **detalhes):
    pasta_logs = "/storage/emulated/0/Download/logs_do_gerenciador"
    os.makedirs(pasta_logs, exist_ok=True)
    log_path = os.path.join(pasta_logs, "log_geral.json")

    log = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "acao": acao,
        "detalhes" : detalhes
        }

    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = {"logs": []}

    dados["logs"].append(log)

    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def exibir_log(caminho_log):
    if not os.path.exists(caminho_log):
        print("Arquivo de log (registros) não encontrado.")
        return

    with open(caminho_log, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    for item in dados["logs"]:
        data = item.get("data", "Desconhecido")
        acao = item.get("acao", "Desconhecido")
        nome_arquivo = item.get("arquivo", "Desconhecido")
        origem = item.get("origem", "Desconhecido")
        destino = item.get("destino", "Desconhecido")
        print(f"{data} | {acao} | {nome_arquivo} | {origem} | {destino}")
