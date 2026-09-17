"""
Evaluador de árboles para la gramática ambigua de la diapositiva 15.
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
Asignatura: Lenguajes de Programación
"""

import sys
import os

from AmbiguousExprVisitor import AmbiguousExprVisitor
from AmbiguousExprReversedVisitor import AmbiguousExprReversedVisitor


class AmbiguousExprEvaluator(AmbiguousExprVisitor):
    def visitProgram(self, ctx):
        return self.visit(ctx.expr())

    def visitAddAmb(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitMulAmb(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitNumAmb(self, ctx):
        text = ctx.NUM().getText()
        return float(text) if "." in text else int(text)


class AmbiguousExprReversedEvaluator(AmbiguousExprReversedVisitor):
    def visitProgram(self, ctx):
        return self.visit(ctx.expr())

    def visitAddAmbRev(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitMulAmbRev(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitNumAmbRev(self, ctx):
        text = ctx.NUM().getText()
        return float(text) if "." in text else int(text)
