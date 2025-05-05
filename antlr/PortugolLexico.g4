lexer grammar PortugolLexico;

// Operadores compostos primeiro para evitar ambiguidades
OP_IGUALDADE: '==';
OP_DIFERENCA: '!=';
OP_MAIOR_IGUAL: '>=';
OP_MENOR_IGUAL: '<=';
OP_INCREMENTO_UNARIO: '++';
OP_DECREMENTO_UNARIO: '--';
OP_SHIFT_LEFT: '<<';
OP_SHIFT_RIGHT: '>>';
OP_ALIAS_BIBLIOTECA: '-->';
OP_MAIS_IGUAL: '+=';
OP_MENOS_IGUAL: '-=';
OP_MULTIPLICACAO_IGUAL: '*=';
OP_DIVISAO_IGUAL: '/=';

// Operadores simples
OP_NAO: 'nao';
OP_E_LOGICO: 'e';
OP_OU_LOGICO: 'ou';
OP_SUBTRACAO: '-';
OP_ADICAO: '+';
OP_MULTIPLICACAO: '*';
OP_DIVISAO: '/';
OP_MOD: '%';
OP_ATRIBUICAO: '=';
OP_MAIOR: '>';
OP_MENOR: '<';
OP_XOR: '^';
OP_OU_BITWISE: '|';
OP_NOT_BITWISE: '~';
E_COMERCIAL: '&';

// Pontuação
ABRE_PARENTESES: '(';
FECHA_PARENTESES: ')';
ABRE_COLCHETES: '[';
FECHA_COLCHETES: ']';
ABRE_CHAVES: '{';
FECHA_CHAVES: '}';
PONTO: '.';
VIRGULA: ',';
PONTOVIRGULA: ';';
DOISPONTOS: ':';

// Palavras-chave
TIPO:
    'real'
    | 'inteiro'
    | 'vazio'
    | 'logico'
    | 'cadeia'
    | 'caracter';
FACA: 'faca';
ENQUANTO: 'enquanto';
PARA: 'para';
SE: 'se';
SENAO: 'senao';
CONSTANTE: 'const';
FUNCAO: 'funcao';
PROGRAMA: 'programa';
ESCOLHA: 'escolha';
CASO: 'caso';
CONTRARIO: 'contrario';
PARE: 'pare';
RETORNE: 'retorne';
INCLUA: 'inclua';
BIBLIOTECA: 'biblioteca';

// Valores lógicos
LOGICO: VERDADEIRO | FALSO;
VERDADEIRO: 'verdadeiro';
FALSO: 'falso';

// Literais
CARACTER: '\'' ( ESC_CARACTER | ~['\\]) '\'';

STRING: '"' ( ESC_SEQ | ~["\\])* '"';

REAL:
    DIGITO+ (PONTO_FRAGMENT DIGITO+)?
    | PONTO_FRAGMENT DIGITO+;

HEXADECIMAL: '0' [xX] SIMBOLO_HEXADECIMAL+;

INT:
    DIGITO+ {
        try:
            int(self.text)
        except ValueError as e:
            raise LexerNoViableAltException(self, None, self._input, 0, e)
    };

// Identificadores
ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

// Comentários
COMENTARIO: '/*' .*? '*/' -> channel(HIDDEN);
COMENTARIO_SIMPLES: '//' .*? ('\n' | EOF) -> channel(HIDDEN);

// Whitespace
WS: [ \t\r\n]+ -> channel(HIDDEN);

// Fragmentos
fragment ESC_SEQ: '\\' [btnfr"'\\] | ESC_UNICODE | ESC_OCTAL;

fragment ESC_CARACTER: ESC_SEQ | '\\\'';

fragment ESC_OCTAL: '\\' [0-3]? [0-7]? [0-7];

fragment ESC_UNICODE:
    '\\u' DIGITO_HEX DIGITO_HEX DIGITO_HEX DIGITO_HEX;

fragment DIGITO_HEX: [0-9a-fA-F];

fragment SIMBOLO_HEXADECIMAL: DIGITO | [a-fA-F];

fragment DIGITO: [0-9];

fragment LETRA: [a-zA-Z];

fragment PONTO_FRAGMENT: '.';
