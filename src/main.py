import sys
import os
from antlr4 import *

# Configura o caminho para encontrar o módulo antlr
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Importa os componentes gerados
from antlr.grammar.PortugolLexer import PortugolLexer
from antlr.grammar.PortugolParser import PortugolParser
from antlr.grammar.PortugolVisitor import PortugolVisitor

class CalculadoraVisitor(PortugolVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitUnario(self, ctx):
        valor = self.visit(ctx.expr())
        return -valor

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == PortugolParser.OP_MULTIPLICACAO:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == PortugolParser.OP_ADICAO:
            return left + right
        else:
            return left - right

    def visitInt(self, ctx):
        return int(ctx.INTEIRO().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())


def main():
    input_text = " ".join(sys.argv[1:]) or "3 + 4 * (2 - 1)"

    input_stream = InputStream(input_text)
    lexer = PortugolLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PortugolParser(tokens)
    tree = parser.prog()

    visitor = CalculadoraVisitor()
    resultado = visitor.visit(tree)
    print(f"Resultado de '{input_text}': {resultado}")

if __name__ == "__main__":
    main()
