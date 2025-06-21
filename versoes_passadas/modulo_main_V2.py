from classe_gerenciador import GerenciadorDeArquivos
from login_ADMIN import autenticar


def exibir_menu():
    print("\n ===== Gerenciador de Arquivos =====")
    print("1 - Exibir Arquivos")
    print("2 - Listar Lixeira")
    print("3 - Renomear Arquivos")
    print("4 - Copiar Arquivos")
    print("5 - Exibir logs (Registro de Ações)")
    print("6 - Criar Arquivos")
    print("7 - Gerenciar ZIPs")
    print("8 - Sair")

def main():
    gerenciador = GerenciadorDeArquivos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pasta = input("Digite o caminho da pasta: ")
            gerenciador.exibir_arquivos(pasta_escolhida=pasta)
        elif opcao == "2":

            gerenciador.listar_lixeira()
        elif opcao == "3":
            pasta = input("Digite o caminho da pasta: ")
            nome_novo = input("Digite o novo nome do arquivo: ")
            gerenciador.renomear_arquivos(pasta_escolhida=pasta, nome_novo=nome_novo)
        elif opcao == "4":
            origem = input("Digite a origem do arquivo: ")
            destino = input("Digite a pasta onde quer copiar o arquivo: ")
            gerenciador.copiar_arquivos(origem, destino)
        elif opcao == "5":
            gerenciador.exibir_logs()
        elif opcao == "6":
        	pasta = input("Digite o caminho da pasta onde deseja criar os arquivos: ")
        	nome = input("Digite o nome base dos arquivos: ")
        	quantidade = int(input("Digite a quantidade de arquivos a criar: "))
        	extensao = input("Digite a extensão (ex: .txt, .jpg): ")
        	gerenciador.criar_arquivos(pasta, quantidade, nome, extensao)
        elif opcao == "7":
            gerenciador.gerenciar_zip()
        elif opcao == "8":
            print("Encerrando , obrigado por usar meu software!")
            break
        else:
            print("Opção inexistente ou inválida, tente novamente.")

if __name__ == "__main__":
    if autenticar(input("Digite a senha de administrador: ")):
            main()
    else:
        print("Acesso negado.")
