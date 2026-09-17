# Generated from ArithmeticExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArithmeticExprParser import ArithmeticExprParser
else:
    from ArithmeticExprParser import ArithmeticExprParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticExprParser.

class ArithmeticExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticExprParser#program.
    def visitProgram(self, ctx:ArithmeticExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#Add.
    def visitAdd(self, ctx:ArithmeticExprParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#Sub.
    def visitSub(self, ctx:ArithmeticExprParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#ToTerm.
    def visitToTerm(self, ctx:ArithmeticExprParser.ToTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#Div.
    def visitDiv(self, ctx:ArithmeticExprParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#ToFactor.
    def visitToFactor(self, ctx:ArithmeticExprParser.ToFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#Mul.
    def visitMul(self, ctx:ArithmeticExprParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#IdFactor.
    def visitIdFactor(self, ctx:ArithmeticExprParser.IdFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#NumFactor.
    def visitNumFactor(self, ctx:ArithmeticExprParser.NumFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExprParser#ParenFactor.
    def visitParenFactor(self, ctx:ArithmeticExprParser.ParenFactorContext):
        return self.visitChildren(ctx)



del ArithmeticExprParser