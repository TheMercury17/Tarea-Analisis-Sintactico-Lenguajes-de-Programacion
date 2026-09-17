# Generated from ArithmeticExpr.g4 by ANTLR 4.13.2
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
        4,1,9,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,46,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,49,0,8,1,0,0,0,
        2,11,1,0,0,0,4,25,1,0,0,0,6,45,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,
        10,1,1,0,0,0,11,12,6,1,-1,0,12,13,3,4,2,0,13,22,1,0,0,0,14,15,10,
        3,0,0,15,16,5,1,0,0,16,21,3,4,2,0,17,18,10,2,0,0,18,19,5,2,0,0,19,
        21,3,4,2,0,20,14,1,0,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,
        0,22,23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,26,6,2,-1,0,26,27,
        3,6,3,0,27,36,1,0,0,0,28,29,10,3,0,0,29,30,5,3,0,0,30,35,3,6,3,0,
        31,32,10,2,0,0,32,33,5,4,0,0,33,35,3,6,3,0,34,28,1,0,0,0,34,31,1,
        0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,
        36,1,0,0,0,39,46,5,7,0,0,40,46,5,8,0,0,41,42,5,5,0,0,42,43,3,2,1,
        0,43,44,5,6,0,0,44,46,1,0,0,0,45,39,1,0,0,0,45,40,1,0,0,0,45,41,
        1,0,0,0,46,7,1,0,0,0,5,20,22,34,36,45
    ]

class ArithmeticExprParser ( Parser ):

    grammarFileName = "ArithmeticExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "program", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    NUM=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ArithmeticExprParser.EOF, 0)

        def getRuleIndex(self):
            return ArithmeticExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ArithmeticExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(ArithmeticExprParser.EOF)
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
            return ArithmeticExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExprParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ArithmeticExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExprParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ArithmeticExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class ToTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticExprParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToTerm" ):
                listener.enterToTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToTerm" ):
                listener.exitToTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTerm" ):
                return visitor.visitToTerm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ArithmeticExprParser.ToTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 20
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExprParser.AddContext(self, ArithmeticExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        self.match(ArithmeticExprParser.T__0)
                        self.state = 16
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExprParser.SubContext(self, ArithmeticExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 18
                        self.match(ArithmeticExprParser.T__1)
                        self.state = 19
                        self.term(0)
                        pass

             
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticExprParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticExprParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticExprParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class ToFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticExprParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToFactor" ):
                listener.enterToFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToFactor" ):
                listener.exitToFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToFactor" ):
                return visitor.visitToFactor(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticExprParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticExprParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExprParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ArithmeticExprParser.ToFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 26
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExprParser.MulContext(self, ArithmeticExprParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(ArithmeticExprParser.T__2)
                        self.state = 30
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExprParser.DivContext(self, ArithmeticExprParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(ArithmeticExprParser.T__3)
                        self.state = 33
                        self.factor()
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticExprParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ArithmeticExprParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumFactor" ):
                listener.enterNumFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumFactor" ):
                listener.exitNumFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumFactor" ):
                return visitor.visitNumFactor(self)
            else:
                return visitor.visitChildren(self)


    class IdFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArithmeticExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdFactor" ):
                listener.enterIdFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdFactor" ):
                listener.exitIdFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdFactor" ):
                return visitor.visitIdFactor(self)
            else:
                return visitor.visitChildren(self)


    class ParenFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticExprParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenFactor" ):
                listener.enterParenFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenFactor" ):
                listener.exitParenFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenFactor" ):
                return visitor.visitParenFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = ArithmeticExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ArithmeticExprParser.IdFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ArithmeticExprParser.ID)
                pass
            elif token in [8]:
                localctx = ArithmeticExprParser.NumFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(ArithmeticExprParser.NUM)
                pass
            elif token in [5]:
                localctx = ArithmeticExprParser.ParenFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(ArithmeticExprParser.T__4)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(ArithmeticExprParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




