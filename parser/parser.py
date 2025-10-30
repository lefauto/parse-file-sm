# parser.py

def _normalize_tag(token_value: str) -> str:
    """
    Remove <, > e / do token de tag e retorna apenas o nome da tag.
    Ex.: "<titulo>" -> "titulo", "</titulo>" -> "titulo", "titulo" -> "titulo"
    """
    if not isinstance(token_value, str):
        return str(token_value)
    s = token_value.strip()
    # remove ângulos se existirem
    if s.startswith("<") and s.endswith(">"):
        s = s[1:-1].strip()
    # remove barra inicial (fechamento)
    if s.startswith("/"):
        s = s[1:].strip()
    return s

def parse(tokens):
    """
    Verifica a validade sintática de uma lista de tokens usando uma pilha.

    tokens: lista de tuplas no formato:
        ('TAG_ABERTURA', 'nome_tag' | '<nome_tag>')
        ('TAG_FECHAMENTO', 'nome_tag' | '</nome_tag>')
        ('TEXTO', 'conteúdo livre')

    Retorna:
        (True, "Sintaxe válida!") se não houver erros
        (False, "Mensagem de erro...") caso encontre erro
    """
    pilha = []

    for idx, token in enumerate(tokens):
        # tolerância a formatos: token pode ter 2 elementos (tipo, valor)
        if not isinstance(token, (list, tuple)) or len(token) < 2:
            return False, f"Erro: token inválido na posição {idx}: {token}"

        tipo, valor = token[0], token[1]

        if tipo == 'TAG_ABERTURA':
            nome = _normalize_tag(valor)
            if nome == "":
                return False, f"Erro: tag de abertura vazia na posição {idx}."
            pilha.append(nome)

        elif tipo == 'TAG_FECHAMENTO':
            nome = _normalize_tag(valor)
            if not pilha:
                return False, f"Erro na posição {idx}: tag de fechamento </{nome}> sem abertura correspondente."
            topo = pilha.pop()
            if topo != nome:
                return False, (f"Erro na posição {idx}: tag de fechamento </{nome}> "
                               f"não corresponde à abertura <{topo}>.")

        elif tipo == 'TEXTO':
            # Texto é ignorado
            continue

        else:
            return False, f"Erro na posição {idx}: tipo de token desconhecido '{tipo}'."

    if pilha:
        return False, f"Erro: tag(s) não fechadas: {', '.join(pilha)}."

    return True, "Sintaxe válida!"
