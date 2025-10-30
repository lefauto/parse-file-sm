from tokenizer.lexer import tokenize
from parser.parser import parse
from tokenizer.utils.functions import listar_arquivos_sm, escolher_arquivo

def validar_arquivo():
    arquivos = listar_arquivos_sm("tokenizer/examples")
    arquivo = escolher_arquivo(arquivos)

    with open(arquivo, "r") as f:
        conteudo = f.read()

    tokens = tokenize(conteudo)
    
    resultado = parse(tokens)
    
    return resultado

if __name__ == "__main__":
    print(validar_arquivo())