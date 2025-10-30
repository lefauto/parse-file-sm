import re

def tokenize(text):
    regex = re.compile(r"(</?\w+>)|([^<>]+)")
    tokens = []

    for match in regex.finditer(text):
        tag = match.group(1)
        texto = match.group(2)

        if tag:
            if tag.startswith("</"):
                tokens.append(("TAG_FECHAMENTO", tag))
            else:
                tokens.append(("TAG_ABERTURA", tag))
        elif texto and texto.strip():
            tokens.append(("TEXTO", texto))

    return tokens

exemplo = "<titulo>Meu Título</titulo>"
print(tokenize(exemplo))
