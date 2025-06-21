def exibir_arquivos(pasta_escolhida=None , filtro_padrao = None):
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
        eturn

        opcoes = {
            "1": lambda arqs: sorted(arqs),
            "2": lambda arqs: sorted(arqs, reverse=True),
            "3": lambda arqs: sorted(arqs, key=os.path.getmtime, reverse=True),
            "4": lambda arqs: sorted(arqs, key=os.path.getmtime),
            "5": lambda arqs: sorted(arqs, key=os.path.getsize),
            "6": lambda arqs: sorted(arqs, key=os.path.getsize, reverse=True),
            "7": lambda arqs: [arq 
            for arq in arqs:
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
