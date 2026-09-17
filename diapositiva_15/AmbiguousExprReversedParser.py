# Generated from AmbiguousExprReversed.g4 by ANTLR 4.13.2
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
        4,1,4,22,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,1,0,1,2,2,0,2,0,0,21,0,4,1,
        0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,
        0,8,9,5,3,0,0,9,18,1,0,0,0,10,11,10,3,0,0,11,12,5,1,0,0,12,17,3,
        2,1,4,13,14,10,2,0,0,14,15,5,2,0,0,15,17,3,2,1,3,16,10,1,0,0,0,16,
        13,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,
        0,20,18,1,0,0,0,2,16,18
    ]

class AmbiguousExprReversedParser ( Parser ):

    grammarFileName = "AmbiguousExprReversed.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_program = 0
    RULE_expr = 1

    ruleNames =  [ "program", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUM=3
    WS=4

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
            return self.getTypedRuleContext(AmbiguousExprReversedParser.ExprContext,0)


        def EOF(self):
            return self.getToken(AmbiguousExprReversedParser.EOF, 0)

        def getRuleIndex(self):
            return AmbiguousExprReversedParser.RULE_program

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

        localctx = AmbiguousExprReversedParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(AmbiguousExprReversedParser.EOF)
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
            return AmbiguousExprReversedParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumAmbRevContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AmbiguousExprReversedParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(AmbiguousExprReversedParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumAmbRev" ):
                listener.enterNumAmbRev(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumAmbRev" ):
                listener.exitNumAmbRev(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumAmbRev" ):
                return visitor.visitNumAmbRev(self)
            else:
                return visitor.visitChildren(self)


    class AddAmbRevContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AmbiguousExprReversedParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AmbiguousExprReversedParser.ExprContext)
            else:
                return self.getTypedRuleContext(AmbiguousExprReversedParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddAmbRev" ):
                listener.enterAddAmbRev(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddAmbRev" ):
                listener.exitAddAmbRev(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddAmbRev" ):
                return visitor.visitAddAmbRev(self)
            else:
                return visitor.visitChildren(self)


    class MulAmbRevContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AmbiguousExprReversedParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AmbiguousExprReversedParser.ExprContext)
            else:
                return self.getTypedRuleContext(AmbiguousExprReversedParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulAmbRev" ):
                listener.enterMulAmbRev(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulAmbRev" ):
                listener.exitMulAmbRev(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulAmbRev" ):
                return visitor.visitMulAmbRev(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AmbiguousExprReversedParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AmbiguousExprReversedParser.NumAmbRevContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 8
            self.match(AmbiguousExprReversedParser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 16
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = AmbiguousExprReversedParser.MulAmbRevContext(self, AmbiguousExprReversedParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 10
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 11
                        self.match(AmbiguousExprReversedParser.T__0)
                        self.state = 12
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = AmbiguousExprReversedParser.AddAmbRevContext(self, AmbiguousExprReversedParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 13
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 14
                        self.match(AmbiguousExprReversedParser.T__1)
                        self.state = 15
                        self.expr(3)
                        pass

             
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




