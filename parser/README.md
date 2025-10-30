# Parser de Sintaxe com Pilha

Este módulo verifica se uma sequência de **tokens** possui **sintaxe válida**, usando o algoritmo clássico de um **autômato de pilha**.

## Lógica do Algoritmo

1. Cria-se uma pilha vazia.
2. Para cada token:
   - Se for uma `TAG_ABERTURA`, empilha o nome da tag.
   - Se for uma `TAG_FECHAMENTO`, desempilha e verifica correspondência.
   - Tokens de `TEXTO` são ignorados.
3. Ao final:
   - Se a pilha estiver vazia → **sintaxe válida**.
   - Caso contrário → **erro: tags abertas não fechadas**.

## Como usar

```python
>>> from parser import parse
>>> tokens = [
...     ('TAG_ABERTURA', 'titulo'),
...     ('TEXTO', 'Olá mundo'),
...     ('TAG_FECHAMENTO', 'titulo')
... ]
>>> parse(tokens)
(True, 'Sintaxe válida!')
```
