from lexer import tokenize
from utils.functions import listar_arquivos_sm, escolher_arquivo

def main():
    arquivos = listar_arquivos_sm("tokenizer/examples")
    arquivo = escolher_arquivo(arquivos)

    with open(arquivo, "r") as f:
        conteudo = f.read()

    tokens = tokenize(conteudo)
    
    return tokens

print(main())
