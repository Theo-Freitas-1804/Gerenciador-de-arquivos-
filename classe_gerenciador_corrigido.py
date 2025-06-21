























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

        
            self.exibir_arquivos(filtro_padrao = "1")
    indices = input("Digite o(s) índice(s):do(s) arquivo(s) que quer compactar:")
    if not hasattr(self , "ultimos_arquivos_exibidos"):
    print("Nenhuma lista disponível")
    return

        selecionados = []
    for i in indices:
    try:
    except (ValueError, IndexError):
    if not selecionados:
    print("Nenhum arquivo válido")
    return

        for caminho in selecionados:
    arquivo_zip.write(caminho , arcname = os.path.basement(caminho))
    print(f"Compactado em {nome_zip}")

            caminho_destino = input("Digite um caminho ou nome padrão (ex: Download): ").strip()
        if caminho_destino in caminhos_padrao:
        caminho_destino = caminhos_padrao[caminho_destino]

                if not os.path.exists(caminho_destino):
        print("O caminho informado está incorreto ou não existe. Tente novamente.")
        return
                                                    caminho_arquivo = os.path.join(self.entrada_atual, arquivo)

                                                    
                                                            if not zipfile.is_zipfile(caminho_arquivo):
            print("O arquivo informado não é um .zip válido.")
            return
        try:

# Criar dados fictícios para o log, ou ajustar de acordo com o seu projeto
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo = arquivo
        origem = caminho_arquivo
        destino = caminho_destino
        registrar_log_geral(data, "Arquivo descompactado", arquivo, origem, destino)

        
                except Exception as e:
        print(f"Erro ao descompactar: {e}")")")

        
        
        
        
        
            descompactar_arquivos(self , arquivo , caminho_destino)
