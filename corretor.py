def corrigir_indentacao(caminho , modo ="análise" , tratar_tabs = True):
    """
    modo:
        - "Analis -> Apenas mostra trechos problemáticose"
        - "Sobrescrever -> Reescreve o arquivo cprrigindo-o com backup"
        - "Novo arquivo -> Cria um novo código com _corrigido.py"
        tratar tabs:
            - True -> Substitui Tabs por 4 espaços
            - False -> Ignora os Tabs
    """
    with open(caminho , "r") as f:
        linhas = f.readlines()
    linhas_corrigidas = []
    erros = []
    for i , linha in enumerate(linhas):
        original = linha
        if tratar_tabs and "\t" in linha:
            erros.append(f"Linhas {i+1}: contém TAB")
            linha = linha.replace("\t" ,' ' * 4 )
        conteudo = linha.lstrip()
        espacos = len(linha) - len(conteudo)
        # linha vazia
        if conteudo == "":
            linhas_corrigidas.append("\n")
            continue
        if espacos % 4 != 0:
            erros.append(f"Linha {i+1}: indentação irregular ({espacos}) espaços)")
            espacos_corrigidos = 4 * (espacos// 4)
            linha = ' ' * espacos_corrigidos + conteudo
        linhas_corrigidas.append(linha)
        if modo == "sobrescrever":
            with open(caminho + ".bak" , "w") as f:
                f.writelines(linhas)
            with open(caminho , "w") as f:
                f.writelines(linhas_corrigidas)
                print(f"Arquivo sobrescrito com correção. Backup salvo com: {caminho}.bak")
        elif modo == "novo_arquivo":
            novo_caminho = caminho.replace(".py" , "_corrigido.py")
            with open(novo_caminho , "w")as f:
                f.writelines(linhas_corrigidas)
                print(f"Novo arquivo salvo como: {novo_caminho}")

        if erros:
                print(" - " , erro)
        else:
            print("Nenhum erro de indentação encontrado")
            return erros

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo Python: ")
    modo = input("Digite 1 para **ver erros**, 2 para **corrigir**: ")

    if modo == '1':
        verificar_indentacao(caminho)
    elif modo == '2':
        corrigir_indentacao(caminho)
    else:
        print("Modo inválido.")
