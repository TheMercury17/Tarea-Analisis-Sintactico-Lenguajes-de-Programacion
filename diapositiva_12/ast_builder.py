"""
Constructor de AST a partir del Parse Tree de ANTLR4.
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
Asignatura: Lenguajes de Programación
"""

import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d11_dir = os.path.join(parent_dir, "diapositiva_11")
if d11_dir not in sys.path:
    sys.path.insert(0, d11_dir)

from ArithmeticExprVisitor import ArithmeticExprVisitor
try:
    from .ast_nodes import BinaryOpNode, NumNode, IdNode, NaryOpNode
except ImportError:
    from ast_nodes import BinaryOpNode, NumNode, IdNode, NaryOpNode


class ASTBuilderVisitor(ArithmeticExprVisitor):
    """
    Transforma el Parse Tree (CST) detallado de la diapositiva 12
    en un Árbol de Sintaxis Abstracta (AST) simplificado.
    """

    def visitProgram(self, ctx):
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return BinaryOpNode("+", left, right)

    def visitSub(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return BinaryOpNode("-", left, right)

    def visitToTerm(self, ctx):
        return self.visit(ctx.term())

    def visitMul(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return BinaryOpNode("*", left, right)

    def visitDiv(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return BinaryOpNode("/", left, right)

    def visitToFactor(self, ctx):
        return self.visit(ctx.factor())

    def visitNumFactor(self, ctx):
        return NumNode(ctx.NUM().getText())

    def visitIdFactor(self, ctx):
        return IdNode(ctx.ID().getText())

    def visitParenFactor(self, ctx):
        return self.visit(ctx.expr())


def flatten_associative_ast(ast_node):
    """
    Convierte operaciones binarias asociativas encadenadas en una forma N-Aria.
    Por ejemplo, (+ (+ 1 2) 3) se convierte en (+ [1, 2, 3]).
    """
    if isinstance(ast_node, BinaryOpNode):
        flattened_left = flatten_associative_ast(ast_node.left)
        flattened_right = flatten_associative_ast(ast_node.right)

        if ast_node.op in ("+", "*"):
            operands = []
            if isinstance(flattened_left, NaryOpNode) and flattened_left.op == ast_node.op:
                operands.extend(flattened_left.operands)
            else:
                operands.append(flattened_left)

            if isinstance(flattened_right, NaryOpNode) and flattened_right.op == ast_node.op:
                operands.extend(flattened_right.operands)
            else:
                operands.append(flattened_right)

            return NaryOpNode(ast_node.op, operands)
        else:
            return BinaryOpNode(ast_node.op, flattened_left, flattened_right)
    return ast_node
