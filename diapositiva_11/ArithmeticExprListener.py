# Generated from ArithmeticExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArithmeticExprParser import ArithmeticExprParser
else:
    from ArithmeticExprParser import ArithmeticExprParser

# This class defines a complete listener for a parse tree produced by ArithmeticExprParser.
class ArithmeticExprListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticExprParser#program.
    def enterProgram(self, ctx:ArithmeticExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#program.
    def exitProgram(self, ctx:ArithmeticExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#Add.
    def enterAdd(self, ctx:ArithmeticExprParser.AddContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#Add.
    def exitAdd(self, ctx:ArithmeticExprParser.AddContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#Sub.
    def enterSub(self, ctx:ArithmeticExprParser.SubContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#Sub.
    def exitSub(self, ctx:ArithmeticExprParser.SubContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#ToTerm.
    def enterToTerm(self, ctx:ArithmeticExprParser.ToTermContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#ToTerm.
    def exitToTerm(self, ctx:ArithmeticExprParser.ToTermContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#Div.
    def enterDiv(self, ctx:ArithmeticExprParser.DivContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#Div.
    def exitDiv(self, ctx:ArithmeticExprParser.DivContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#ToFactor.
    def enterToFactor(self, ctx:ArithmeticExprParser.ToFactorContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#ToFactor.
    def exitToFactor(self, ctx:ArithmeticExprParser.ToFactorContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#Mul.
    def enterMul(self, ctx:ArithmeticExprParser.MulContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#Mul.
    def exitMul(self, ctx:ArithmeticExprParser.MulContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#IdFactor.
    def enterIdFactor(self, ctx:ArithmeticExprParser.IdFactorContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#IdFactor.
    def exitIdFactor(self, ctx:ArithmeticExprParser.IdFactorContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#NumFactor.
    def enterNumFactor(self, ctx:ArithmeticExprParser.NumFactorContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#NumFactor.
    def exitNumFactor(self, ctx:ArithmeticExprParser.NumFactorContext):
        pass


    # Enter a parse tree produced by ArithmeticExprParser#ParenFactor.
    def enterParenFactor(self, ctx:ArithmeticExprParser.ParenFactorContext):
        pass

    # Exit a parse tree produced by ArithmeticExprParser#ParenFactor.
    def exitParenFactor(self, ctx:ArithmeticExprParser.ParenFactorContext):
        pass



del ArithmeticExprParser