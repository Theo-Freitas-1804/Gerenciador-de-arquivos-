import os
import json
from datetime import datetime

def registrar_log_lixeira(acao, arquivo, origem=None, destino=None):
    pasta_logs = "/storage/emulated/0/Download/logs_do_gerenciador"
    os.makedirs(pasta_logs, exist_ok=True)
    log_path = os.path.join(pasta_logs, "log_lixeira.json")
    log = {
        "data": datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
        "acao": acao,
        "arquivo": arquivo,
        "origem": origem,
        "destino": destino
    }
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = {"logs": []}

    dados["logs"].append(log)

    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def recuperar_origem_arquivo(nome_arquivo, log_path="/storage/emulated/0/Download/logs_do_gerenciador/log_lixeira.json"):
    if not os.path.exists(log_path):
        print("Log da lixeira não encontrado.")
        return None

    with open(log_path, "r", encoding="utf-8") as f:
        dados = json.load(f)

    for log in reversed(dados.get("logs", [])):
        if log.get("arquivo") == nome_arquivo and log.get("origem"):
            return log["origem"]

    print("Origem do arquivo não encontrada no log.")
    return None

def exibir_log_lixeira(caminho_log):
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