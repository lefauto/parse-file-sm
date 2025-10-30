from parser import parse

def main():
    arquivos = [
                [('TAG_ABERTURA', '<titulo>'), ('TEXTO', 'tag de fechamento errada'), ('TAG_FECHAMENTO', '</titul>')], # 1 Inválido
                [('TAG_FECHAMENTO', '</titulo>'), ('TEXTO', 'texto solto sem abertura\n')], # 2 Inválido
                [('TAG_ABERTURA', '<titulo>'), ('TEXTO', 'sem fechamento'), ('TAG_ABERTURA', '<titulo>')], # 3 Inválido
                [('TAG_ABERTURA', '<HTML>'), ('TAG_ABERTURA', '<head>'), ('TAG_ABERTURA', '<title>'), ('TEXTO', 'Simple Markup'), ('TAG_FECHAMENTO', '</title>'), ('TAG_FECHAMENTO', '</head>'), ('TAG_ABERTURA', '<body>'), ('TAG_ABERTURA', '<a>'), ('TEXTO', 'teste do analisador lexico.'), ('TAG_FECHAMENTO', '</a>'), ('TAG_FECHAMENTO', '</body>'), ('TAG_FECHAMENTO', '</HTML>')], # 1 Válido
                [('TAG_ABERTURA', '<titulo>'), ('TEXTO', 'Meu Título'), ('TAG_FECHAMENTO', '</titulo>')], # 2 Válido
                [('TAG_ABERTURA', '<livro>'), ('TAG_ABERTURA', '<titulo>'), ('TEXTO', 'Chainsaw Man'), ('TAG_FECHAMENTO', '</titulo>'), ('TAG_ABERTURA', '<autor>'), ('TEXTO', 'Tatsuki Fujimoto'), ('TAG_FECHAMENTO', '</autor>'), ('TAG_FECHAMENTO', '</livro>')] # 3 Válido
            ]
    
    print("Escolha um arquivo token\n")
    for i, valor in enumerate(arquivos, start=1):
        print(f"{i}. {valor}")
    print()

    while True:
        try:
            escolha = int(input("Digite o número do arquivo: "))
            if 1 <= escolha <= len(arquivos):
                conteudo = arquivos[escolha - 1]
                break
            else:
                print("Número inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas o número correspondente.")

    tokens = parse(conteudo)
    
    return tokens

print(main())
