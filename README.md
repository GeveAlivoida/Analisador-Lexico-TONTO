# Analisador Léxico para TONTO (Textual Ontology Language)

**Disciplina:** Compiladores — UFERSA/CCEN/Departamento de Computação   
**Professor:** Patrício de Alencar Silva    
**Ferramenta:** PLY (Python Lex-Yacc)   
**Grupo**: João Vitor Russo Liberalino, Alian Aguiar, Francisco Bisneto

## 1. Objetivo

Este projeto implementa um analisador léxico para a linguagem TONTO,
uma sintaxe textual para especificação de ontologias baseada em OntoUML.
O analisador reconhece os tokens definidos na especificação da disciplina e
produz duas saídas para cada arquivo de entrada:

1. **Visão analítica** — todos os tokens reconhecidos, na ordem em que aparecem,
   com número de linha e coluna.
2. **Tabela de síntese** — quantidade de tokens por categoria (classes, relações,
   estereótipos, palavras reservadas, instâncias, tipos nativos, novos tipos,
   meta-atributos, números, símbolos e erros).

## 2. Estrutura do projeto

```
.
└── testes/
    ├── bandas_certo.tonto   # Código válido contendo ontologia de bandas e instrumentos
    ├── bandas_errado.tonto  # Mesma ontologia mas com erros intencionais para testar tratamento de erro
    └── musica.tonto         # Ontologia sobre música, com datatypes e generalization sets, importada por bandas_certo
├── lexer.py          # Definição dos tokens e expressões regulares
├── main.py           # Execução do lexer sobre os arquivos de teste e impressão dos relatórios
├── requirements.txt  # Dependências (para esse projeto, apenas o ply)
```

## 3. Categorias de token reconhecidas

| Token                  | Descrição                                                                 | Exemplos                                  |
|------------------------|----------------------------------------------------------------------------|--------------------------------------------|
| `SIMBOLO`              | Pontuação e operadores da linguagem                                      | `{ } ( ) [ ] .. <>-- --<> * @ :`                   |
| `ESTEREOTIPO_CLASSE`   | Estereótipos ontológicos de classe (OntoUML)                             | `kind`, `role`, `phase`, `category`               |
| `ESTEREOTIPO_RELACAO`  | Estereótipos ontológicos de relação                                      | `material`, `mediation`, `characterization`       |
| `PALAVRA_RESERVADA`    | Palavras-chave estruturais da linguagem                                  | `package`, `import`, `genset`, `disjoint`     |
| `TIPO_NATIVO`          | Tipos de dado primitivos                                                 | `number`, `string`, `boolean`, `date`        |
| `META_ATRIBUTO`        | Modificadores de atributo                                                | `ordered`, `const`, `derived`, `subsets`     |
| `NOVO_TIPO`            | Datatypes definidos pelo usuário, contendo o sufixo `DataType`           | `CPFDataType`, `duracaoDataType`        |
| `INSTANCIA`            | Nomes de indivíduos (letra inicial + número final)                       | `Planeta1`, `banda02`                |
| `CLASSE`               | Nomes de classes (inicial maiúscula)                                     | `Musico`, `Banda`, `Disco`                  |
| `RELACAO`              | Nomes de relações/atributos (inicial minúscula)                          | `toca`, `hasParent`, `nome`                   |
| `NUMERO`               | Literais numéricos inteiros                                              | `1`, `123`                    |
| `ERRO`                 | Identificadores que não se encaixam em nenhuma regra válida              | tokens malformados              |

A precedência das regras segue a ordem de definição em `lexer.py`: estereótipos
e palavras reservadas são verificados antes das regras genéricas de
`CLASSE`/`RELACAO`, o que evita que uma palavra-chave como `kind` seja
capturada como nome de relação comum.

## 4. Como executar

```bash
pip install -r requirements.txt
python3 main.py
```

O script processa, em sequência, os três arquivos de teste da pasta `testes/`
(`bandas_certo.tonto`, `bandas_errado.tonto` e `musica.tonto`), imprimindo para
cada um a visão analítica de tokens e a tabela de síntese.

## 5. Arquivos de teste

- **`bandas_certo.tonto`**: ontologia sintaticamente correta sobre bandas
  musicais, instrumentos e músicos. Exercita praticamente todas as categorias
  de token, incluindo `genset`, meta-atributos (`derived`, `const`, `ordered`),
  instâncias (`Violao1`, `banda02`) e relações estereotipadas.
- **`bandas_errado.tonto`**: versão da mesma ontologia com erros propositais
  (palavra-chave grafada errado, nome de classe iniciando com número,
  caracteres inválidos como `&`, `$`, `#`, `%`, identificador iniciando com
  `_`, número solto), usada para validar o tratamento de erros léxicos.
- **`musica.tonto`**: ontologia sobre composição musical, com foco em
  `datatype`s compostos (`notaMusicalDataType`, `assinaturaTempoDataType`) e em
  um *generalization set* completo (`complete genset`).

## 6. Tratamento de erros

Caracteres que não correspondem a nenhuma regra de token disparam a função
`t_error`, que imprime uma mensagem indicando o caractere inválido e a linha
onde ele foi encontrado, e então descarta o caractere para permitir que a
análise continue até o fim do arquivo (o lexer não interrompe a execução por
causa de um erro pontual).

## 7. Limitações conhecidas

Estas limitações foram identificadas ao executar o analisador sobre os três
arquivos de teste:

- **Comentários (`//`) não são ignorados.** O lexer atual não possui uma regra
  para descartar comentários de linha; por isso, o texto de um comentário é
  tokenizado normalmente (e cada `/` isolado gera um erro léxico). Isso é
  visível na análise de `bandas_errado.tonto`, que contém comentários
  explicativos.
- **Vírgulas (`,`) não são reconhecidas como símbolo válido.** A linguagem usa
  vírgulas para separar itens em listas (ex.: enums, `specifics`), mas o
  conjunto de símbolos definido em `t_SIMBOLO` não inclui `,`; cada ocorrência
  gera "Caractere inválido: ','".
  Ambas as limitações persistem no arquivo `bandas_certo.tonto`, mesmo sendo
  ele sintaticamente correto segundo a especificação da linguagem — por isso
  aparecem mensagens de erro léxico mesmo nesse arquivo de teste "correto".
- **A regra `t_ERRO` é bastante ampla** e captura qualquer sequência
  alfanumérica que não se encaixe nas regras anteriores, mas na prática pouco
  é classificado como `ERRO` porque `t_RELACAO` (minúsculas) e `t_CLASSE`
  (maiúsculas) já cobrem quase todos os identificadores válidos. Também não
  pudemos implementar o tratamento de erro refinado com correção.

## 8. Referências

Ver seção de referências do enunciado do trabalho (Coutinho et al. 2024;
Guizzardi et al. 2018; especificações W3C de RDF e OWL; documentação da
ferramenta Tonto de Matheus Lenke).