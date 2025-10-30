import os

def listar_arquivos_sm(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".sm")]
    return arquivos

def escolher_arquivo(arquivos):
    print("Escolha um arquivo .sm para tokenizar\n")
    for i, nome in enumerate(arquivos, start=1):
        print(f"{i}. {nome}")
    print()

    while True:
        try:
            escolha = int(input("Digite o número do arquivo: "))
            if 1 <= escolha <= len(arquivos):
                return "tokenizer/examples/" + arquivos[escolha - 1]
            else:
                print("Número inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas o número correspondente.")