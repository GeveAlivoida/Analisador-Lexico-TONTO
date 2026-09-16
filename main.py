from lexer import lexer

# Dicionário que armazena a quantidade de tokens de cada tipo
tabela = {
    'SIMBOLO': 0,
    "ESTEREOTIPO_CLASSE": 0,
    "ESTEREOTIPO_RELACAO": 0,
    "PALAVRA_RESERVADA": 0,
    "CLASSE": 0,
    "RELACAO": 0,
    "INSTANCIA": 0,
    "TIPO_NATIVO": 0,
    "NOVO_TIPO": 0,
    "META_ATRIBUTO": 0,
    "NUMERO": 0,
    "ERRO": 0,
}


# Abrindo e lendo o arquivo de entrada
arquivo = open("testes/teste.tonto", "r")
codigo = arquivo.read()

# Inicializando o analisador léxico
lexer.lineno = 1
lexer.input(codigo)

# Variáveis que contam o número da linha e a coluna do token atual 
contador = 0
linhaAnterior = 1

# Laço do analizador léxico
print("|=======================================================================|")
print("|================== VISÃO ANALÍTICA DE TODOS OS TOKENS =================|")
for token in lexer:
    print("|-----------------------------------------------------------------------|")
    
    # Contador de colunas de uma linhas
    if token.lineno == linhaAnterior:
        contador += 1
    else:
        contador = 1

    # Atualiza a quantidade de tokens do tipo correto
    if token.type in tabela:
        tabela[token.type] += 1
    
    print(f"| Linha {token.lineno:<5}| Coluna {contador:<5}| {token.type:<20} → {token.value:<20}|")
    linhaAnterior = token.lineno
print("|=======================================================================|")



# Tabela de síntese dos tokens
print("\n|======================================|")
print("|========== TABELA DE SÍNTESE =========|")
print("|--------------------------------------|")
print("| Tipo                | Quantidade     |")
for tipo, quantidade in tabela.items():
    print("|--------------------------------------|")
    print(f"| {tipo:<20}| {quantidade:<15}|")
print("|--------------------------------------|")

arquivo.close()