# Generated from Portugol.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,29,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,16,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,1,0,1,2,2,0,2,0,2,1,0,3,4,1,0,5,6,30,0,4,1,0,0,0,2,15,1,0,0,
        0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,9,5,6,0,0,9,
        16,3,2,1,5,10,16,5,7,0,0,11,12,5,1,0,0,12,13,3,2,1,0,13,14,5,2,0,
        0,14,16,1,0,0,0,15,7,1,0,0,0,15,10,1,0,0,0,15,11,1,0,0,0,16,25,1,
        0,0,0,17,18,10,4,0,0,18,19,7,0,0,0,19,24,3,2,1,5,20,21,10,3,0,0,
        21,22,7,1,0,0,22,24,3,2,1,4,23,17,1,0,0,0,23,20,1,0,0,0,24,27,1,
        0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,25,1,0,0,0,3,15,
        23,25
    ]

class PortugolParser ( Parser ):

    grammarFileName = "Portugol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP_MULTIPLICACAO", 
                      "OP_DIVISAO", "OP_ADICAO", "OP_SUBTRACAO", "INTEIRO", 
                      "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP_MULTIPLICACAO=3
    OP_DIVISAO=4
    OP_ADICAO=5
    OP_SUBTRACAO=6
    INTEIRO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PortugolParser.ExprContext,0)


        def EOF(self):
            return self.getToken(PortugolParser.EOF, 0)

        def getRuleIndex(self):
            return PortugolParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PortugolParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(PortugolParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PortugolParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PortugolParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PortugolParser.ExprContext)
            else:
                return self.getTypedRuleContext(PortugolParser.ExprContext,i)

        def OP_MULTIPLICACAO(self):
            return self.getToken(PortugolParser.OP_MULTIPLICACAO, 0)
        def OP_DIVISAO(self):
            return self.getToken(PortugolParser.OP_DIVISAO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PortugolParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PortugolParser.ExprContext)
            else:
                return self.getTypedRuleContext(PortugolParser.ExprContext,i)

        def OP_ADICAO(self):
            return self.getToken(PortugolParser.OP_ADICAO, 0)
        def OP_SUBTRACAO(self):
            return self.getToken(PortugolParser.OP_SUBTRACAO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PortugolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PortugolParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class UnarioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PortugolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP_SUBTRACAO(self):
            return self.getToken(PortugolParser.OP_SUBTRACAO, 0)
        def expr(self):
            return self.getTypedRuleContext(PortugolParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PortugolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEIRO(self):
            return self.getToken(PortugolParser.INTEIRO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PortugolParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = PortugolParser.UnarioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(PortugolParser.OP_SUBTRACAO)
                self.state = 9
                self.expr(5)
                pass
            elif token in [7]:
                localctx = PortugolParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(PortugolParser.INTEIRO)
                pass
            elif token in [1]:
                localctx = PortugolParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(PortugolParser.T__0)
                self.state = 12
                self.expr(0)
                self.state = 13
                self.match(PortugolParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PortugolParser.MulDivContext(self, PortugolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 18
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = PortugolParser.AddSubContext(self, PortugolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 21
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expr(4)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




