try:
    shutil.move(caminho_antigo , caminho_destino)
    print(f"Arquivo {nome_arquivo} movido com sucesso para {caminho_destino}")
    registrar_log(f"Arquivo '{nome_arquivo}' movido de '{pasta_antiga}' para '{pasta_nova}'")
except Exception as e:
    print(f"Erro ao mover o arquivo '{nome_arquivo}': {e}")
