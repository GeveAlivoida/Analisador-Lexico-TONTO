import ply.lex as lex

#lista de tokens até o momento

tokens = (
    'SIMBOLO',
    'ESTEREOTIPO_CLASSE',
    'ESTEREOTIPO_RELACAO',
    'PALAVRA_RESERVADA',
    'CLASSE',
    'RELACAO',
    'INSTANCIA',
    'TIPO_NATIVO',
    'NOVO_TIPO',
    'META_ATRIBUTO',
)

# Regras para reconhecer os símbolos

def t_SIMBOLO(t):
    r'\.\.|<>--|--<>|\{|\}|\(|\)|\[|\]|\*|@|:'
    return t

def t_ESTEREOTIPO_CLASSE(t):
    r'event|situation|process|category|mixin|phaseMixin|roleMixin|historicalRoleMixin|kind|collective|quantity|quality|mode|intrisicMode|extrinsicMode|subkind|phase|role|historicalRole'
    return t 

def t_ESTEREOTIPO_RELACAO(t):
    r'material|derivation|comparative|mediation|characterization|externalDependence|subCollectionOf|subQualityOf|componentOf|instantiation|memberOf|termination|participational|participation|historicalDependence|creation|manifestation|bringsAbout|triggers|composition|aggregation|inherence|value|formal|constitution'
    return t 

def t_PALAVRA_RESERVADA(t):
    r'genset|disjoint|complete|general|specifics|where|package|import|functional-complexes'
    return t

def t_TIPO_NATIVO(t):
    r'number|string|boolean|date|time|datetime'
    return t


def t_META_ATRIBUTO(t):
    r'ordered|const|derived|subsets|redefines'
    return t


def NOVO_TIPO(t):
    r'[A-Za-z_]+Datatype'
    return t

def t_CLASSE(t):
    r'[A-Z][A-Za-z_]*'
    return t

def t_RELACAO(t):
    r'[a-z][A-Za-z_]*'
    return t

def t_INSTANCIA(t):
    r'[a-z][A-Za-z_]*'
    return t



# Ignora espaços e tabulações
t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

def t_NOVA_LINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
   
# analisador lexico em ação 

lexer = lex.lex()