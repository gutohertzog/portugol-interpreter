# Generated from Portugol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser

# This class defines a complete generic visitor for a parse tree produced by PortugolParser.

class PortugolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PortugolParser#prog.
    def visitProg(self, ctx:PortugolParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#MulDiv.
    def visitMulDiv(self, ctx:PortugolParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#AddSub.
    def visitAddSub(self, ctx:PortugolParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#Parens.
    def visitParens(self, ctx:PortugolParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#Unario.
    def visitUnario(self, ctx:PortugolParser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#Int.
    def visitInt(self, ctx:PortugolParser.IntContext):
        return self.visitChildren(ctx)



del PortugolParser