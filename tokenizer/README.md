## Tokenizer

Este projeto implementa um analisador léxico (lexer) simples em Python para a linguagem de marcação fictícia SimpleMarkup (.sm).  
Ele identifica tags de abertura, tags de fechamento e textos contidos entre elas.


## Funcionalidades

- Lê arquivos .sm e os converte em listas de tokens.
- Diferencia os tipos de tokens:
  - TAG_ABERTURA, <tag>
  - TAG_FECHAMENTO, </tag>
  - TEXTO, texto entre tags
- Exibe os tokens formatados diretamente no terminal.

## Como Rodar

Rodar o arquivo main.py, ele tem uma interface no terminal para navegar entre os arquivos tokenizáveis.

