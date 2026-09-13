from lexer import lexer

# Texto que será analisado

codigo = """
Abel ha
...
number
A
b
"""

lexer.input(codigo)

# Pega os tokens encontrados
for token in lexer:
    print(f"{token.type} → {token.value}")