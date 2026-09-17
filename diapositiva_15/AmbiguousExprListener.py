# Generated from AmbiguousExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AmbiguousExprParser import AmbiguousExprParser
else:
    from AmbiguousExprParser import AmbiguousExprParser

# This class defines a complete listener for a parse tree produced by AmbiguousExprParser.
class AmbiguousExprListener(ParseTreeListener):

    # Enter a parse tree produced by AmbiguousExprParser#program.
    def enterProgram(self, ctx:AmbiguousExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by AmbiguousExprParser#program.
    def exitProgram(self, ctx:AmbiguousExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by AmbiguousExprParser#MulAmb.
    def enterMulAmb(self, ctx:AmbiguousExprParser.MulAmbContext):
        pass

    # Exit a parse tree produced by AmbiguousExprParser#MulAmb.
    def exitMulAmb(self, ctx:AmbiguousExprParser.MulAmbContext):
        pass


    # Enter a parse tree produced by AmbiguousExprParser#NumAmb.
    def enterNumAmb(self, ctx:AmbiguousExprParser.NumAmbContext):
        pass

    # Exit a parse tree produced by AmbiguousExprParser#NumAmb.
    def exitNumAmb(self, ctx:AmbiguousExprParser.NumAmbContext):
        pass


    # Enter a parse tree produced by AmbiguousExprParser#AddAmb.
    def enterAddAmb(self, ctx:AmbiguousExprParser.AddAmbContext):
        pass

    # Exit a parse tree produced by AmbiguousExprParser#AddAmb.
    def exitAddAmb(self, ctx:AmbiguousExprParser.AddAmbContext):
        pass



del AmbiguousExprParser