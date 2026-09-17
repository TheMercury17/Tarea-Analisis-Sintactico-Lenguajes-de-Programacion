"""
Evaluador de expresiones aritméticas para la diapositiva 11/42.
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
Asignatura: Lenguajes de Programación
"""

try:
    from .ArithmeticExprVisitor import ArithmeticExprVisitor
except ImportError:
    from ArithmeticExprVisitor import ArithmeticExprVisitor


class ArithmeticEvaluator(ArithmeticExprVisitor):
    def __init__(self, symbol_table=None):
        super().__init__()
        self.symbol_table = symbol_table or {}

    def visitProgram(self, ctx):
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return left + right

    def visitSub(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return left - right

    def visitToTerm(self, ctx):
        return self.visit(ctx.term())

    def visitMul(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return left * right

    def visitDiv(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        if right == 0:
            raise ZeroDivisionError("Error: División por cero")
        return left / right

    def visitToFactor(self, ctx):
        return self.visit(ctx.factor())

    def visitNumFactor(self, ctx):
        text = ctx.NUM().getText()
        return float(text) if "." in text else int(text)

    def visitIdFactor(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.symbol_table:
            return self.symbol_table[var_name]
        raise NameError(f"Variable '{var_name}' no definida en la tabla de símbolos")

    def visitParenFactor(self, ctx):
        return self.visit(ctx.expr())
