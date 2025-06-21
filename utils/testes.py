from core.gerenciador_base import GerenciadorDeArquivos

def sandbox_testes_zip():
    gerenciador = GerenciadorDeArquivos()
    while True:
        print("\n📦 Deseja descompactar um arquivo?")
        opcao = input("Digite S para sim ou N para não: ").strip().lower()
        if opcao == "s":
            sucesso = gerenciador.descompactar_arquivos()
        if not sucesso:
            print("❗ Algo deu errado durante a descompactação.")
        elif opcao == "n":
            print("Encerrando testes.")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")
