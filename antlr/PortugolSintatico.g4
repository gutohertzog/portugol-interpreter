grammar PortugolSintatico;

options {
    tokenVocab = PortugolLexico;
}

arquivo:
    PROGRAMA ID ABRE_CHAVES (inclusaoBiblioteca)* (
        declaracaoGlobal
        | declaracaoFuncao
    )* FECHA_CHAVES;

inclusaoBiblioteca:
    INCLUA BIBLIOTECA ID (OP_ALIAS_BIBLIOTECA ID)? PONTOVIRGULA;

declaracaoGlobal: listaDeclaracoes PONTOVIRGULA;

listaDeclaracoes: (CONSTANTE)? TIPO declaracao (
        VIRGULA declaracao
    )*;

declaracao:
    declaracaoVariavel
    | declaracaoArray
    | declaracaoMatriz;

declaracaoVariavel: ID (OP_ATRIBUICAO expressao)?;

declaracaoArray:
    ID ABRE_COLCHETES expr FECHA_COLCHETES (
        OP_ATRIBUICAO inicializacaoArray
    )?;

declaracaoMatriz:
    ID ABRE_COLCHETES expr FECHA_COLCHETES ABRE_COLCHETES expr FECHA_COLCHETES (
        OP_ATRIBUICAO inicializacaoMatriz
    )?;

inicializacaoArray:
    ABRE_CHAVES (expressao (VIRGULA expressao)*)? FECHA_CHAVES;

inicializacaoMatriz:
    ABRE_CHAVES (
        inicializacaoArray (VIRGULA inicializacaoArray)*
    )? FECHA_CHAVES;

declaracaoFuncao:
    FUNCAO (TIPO | 'vazio') ID parametrosFuncao ABRE_CHAVES comando* FECHA_CHAVES;

parametrosFuncao:
    ABRE_PARENTESES (parametro (VIRGULA parametro)*)? FECHA_PARENTESES;

parametro:
    TIPO (
        ABRE_COLCHETES FECHA_COLCHETES (
            ABRE_COLCHETES FECHA_COLCHETES
        )?
    )? ID;

comando:
    declaracaoLocal PONTOVIRGULA    # comandoDeclaracao
    | estruturaControle             # comandoControle
    | chamadaFuncao PONTOVIRGULA    # comandoChamadaFuncao
    | atribuicao PONTOVIRGULA       # comandoAtribuicao
    | retorne PONTOVIRGULA          # comandoRetorno
    | pare PONTOVIRGULA             # comandoPare;

declaracaoLocal: (CONSTANTE)? TIPO declaracao (
        VIRGULA declaracao
    )*;

estruturaControle:
    se              # controleSe
    | enquanto      # controleEnquanto
    | facaEnquanto  # controleFacaEnquanto
    | para          # controlePara
    | escolha       # controleEscolha;

se:
    SE ABRE_PARENTESES expressao FECHA_PARENTESES blocoComandos (
        senao
    )?;

senao: SENAO blocoComandos;

enquanto:
    ENQUANTO ABRE_PARENTESES expressao FECHA_PARENTESES blocoComandos;

facaEnquanto:
    FACA blocoComandos ENQUANTO ABRE_PARENTESES expressao FECHA_PARENTESES PONTOVIRGULA;

para:
    PARA ABRE_PARENTESES (
        declaracaoLocal
        | atribuicao
        | /* vazio */
    ) PONTOVIRGULA expressao? PONTOVIRGULA (
        atribuicao
        | expressao
    )? FECHA_PARENTESES blocoComandos;

escolha:
    ESCOLHA ABRE_PARENTESES expressao FECHA_PARENTESES ABRE_CHAVES caso+ FECHA_CHAVES;

caso: CASO (CONTRARIO | expressao) DOISPONTOS blocoComandos;

blocoComandos: ABRE_CHAVES comando* FECHA_CHAVES | comando;

atribuicao: (acessoVariavel | acessoArray | acessoMatriz) OP_ATRIBUICAO expressao;

acessoVariavel: ID;

acessoArray: ID ABRE_COLCHETES expr FECHA_COLCHETES;

acessoMatriz:
    ID ABRE_COLCHETES expr FECHA_COLCHETES ABRE_COLCHETES expr FECHA_COLCHETES;

retorne: RETORNE expressao?;

pare: PARE;

expressao: exprLogica;

exprLogica:
    exprLogica OP_E_LOGICO exprRelacional       # exprLogicaE
    | exprLogica OP_OU_LOGICO exprRelacional    # exprLogicaOu
    | exprRelacional                            # exprLogicaRelacional;

exprRelacional:
    exprArit OP_IGUALDADE exprArit      # exprIgualdade
    | exprArit OP_DIFERENCA exprArit    # exprDiferenca
    | exprArit OP_MAIOR exprArit        # exprMaior
    | exprArit OP_MENOR exprArit        # exprMenor
    | exprArit OP_MAIOR_IGUAL exprArit  # exprMaiorIgual
    | exprArit OP_MENOR_IGUAL exprArit  # exprMenorIgual
    | exprArit                          # exprRelacionalArit;

exprArit:
    exprArit OP_ADICAO exprTermo        # exprAdicao
    | exprArit OP_SUBTRACAO exprTermo   # exprSubtracao
    | exprTermo                         # exprAritTermo;

exprTermo:
    exprTermo OP_MULTIPLICACAO exprFator    # exprMultiplicacao
    | exprTermo OP_DIVISAO exprFator        # exprDivisao
    | exprTermo OP_MOD exprFator            # exprModulo
    | exprFator                             # exprTermoFator;

exprFator:
    OP_SUBTRACAO exprFator                          # exprNegativo
    | OP_NAO exprFator                              # exprNegacaoLogica
    | OP_NOT_BITWISE exprFator                      # exprNegacaoBitwise
    | ABRE_PARENTESES expressao FECHA_PARENTESES    # exprParenteses
    | literal                                       # exprLiteral
    | chamadaFuncao                                 # exprChamadaFuncao
    | acessoVariavel                                # exprAcessoVariavel
    | acessoArray                                   # exprAcessoArray
    | acessoMatriz                                  # exprAcessoMatriz
    | incrementoDecremento                          # exprIncrementoDecremento;

incrementoDecremento:
    OP_INCREMENTO_UNARIO acessoVariavel     # exprIncrementoPrefixado
    | OP_DECREMENTO_UNARIO acessoVariavel   # exprDecrementoPrefixado
    | acessoVariavel OP_INCREMENTO_UNARIO   # exprIncrementoPosfixado
    | acessoVariavel OP_DECREMENTO_UNARIO   # exprDecrementoPosfixado;

chamadaFuncao: (ID PONTO)? ID ABRE_PARENTESES listaArgumentos? FECHA_PARENTESES;

listaArgumentos: expressao (VIRGULA expressao)*;

literal:
    INT             # literalInteiro
    | HEXADECIMAL   # literalHexadecimal
    | REAL          # literalReal
    | LOGICO        # literalLogico
    | CARACTER      # literalCaracter
    | STRING        # literalString;
