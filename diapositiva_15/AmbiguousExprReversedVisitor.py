# Generated from AmbiguousExprReversed.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AmbiguousExprReversedParser import AmbiguousExprReversedParser
else:
    from AmbiguousExprReversedParser import AmbiguousExprReversedParser

# This class defines a complete generic visitor for a parse tree produced by AmbiguousExprReversedParser.

class AmbiguousExprReversedVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AmbiguousExprReversedParser#program.
    def visitProgram(self, ctx:AmbiguousExprReversedParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprReversedParser#NumAmbRev.
    def visitNumAmbRev(self, ctx:AmbiguousExprReversedParser.NumAmbRevContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprReversedParser#AddAmbRev.
    def visitAddAmbRev(self, ctx:AmbiguousExprReversedParser.AddAmbRevContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprReversedParser#MulAmbRev.
    def visitMulAmbRev(self, ctx:AmbiguousExprReversedParser.MulAmbRevContext):
        return self.visitChildren(ctx)



del AmbiguousExprReversedParser