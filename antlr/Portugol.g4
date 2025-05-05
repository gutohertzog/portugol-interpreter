grammar Portugol;

// Regras da linguagem
prog: expr EOF;

expr:
    '-' expr # Unario
    | expr op = (OP_MULTIPLICACAO | OP_DIVISAO) expr # MulDiv
    | expr op = (OP_ADICAO | OP_SUBTRACAO) expr # AddSub
    | INTEIRO # Int
    | '(' expr ')' # Parens;

// Tokens
OP_MULTIPLICACAO: '*';
OP_DIVISAO: '/';
OP_ADICAO: '+';
OP_SUBTRACAO: '-';

INTEIRO: [0-9]+;

// whitespace (linha em branco)
WS: [ \t\r\n]+ -> skip;
