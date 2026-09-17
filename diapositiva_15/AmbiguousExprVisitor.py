# Generated from AmbiguousExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AmbiguousExprParser import AmbiguousExprParser
else:
    from AmbiguousExprParser import AmbiguousExprParser

# This class defines a complete generic visitor for a parse tree produced by AmbiguousExprParser.

class AmbiguousExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AmbiguousExprParser#program.
    def visitProgram(self, ctx:AmbiguousExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprParser#MulAmb.
    def visitMulAmb(self, ctx:AmbiguousExprParser.MulAmbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprParser#NumAmb.
    def visitNumAmb(self, ctx:AmbiguousExprParser.NumAmbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprParser#AddAmb.
    def visitAddAmb(self, ctx:AmbiguousExprParser.AddAmbContext):
        return self.visitChildren(ctx)



del AmbiguousExprParser