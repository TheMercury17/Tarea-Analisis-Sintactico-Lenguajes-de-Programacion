"""
Definición de las diferentes estructuras de nodos para el Árbol de Sintaxis Abstracta (AST).
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
Asignatura: Lenguajes de Programación
Diapositiva 12/42: Formas de AST y comparación con Parse Tree (CST)
"""

from abc import ABC, abstractmethod
import json


class ASTNode(ABC):
    """Clase base para todos los nodos del AST."""

    @abstractmethod
    def evaluate(self, env=None):
        pass

    @abstractmethod
    def to_sexpr(self):
        """Representación en S-Expression (estilo Lisp/Tupla)."""
        pass

    @abstractmethod
    def to_dict(self):
        """Representación estructurada tipo JSON / Diccionario."""
        pass

    @abstractmethod
    def to_ascii_tree(self, indent="", is_last=True, use_ascii=False):
        """Representación visual en árbol jerárquico."""
        pass

    @abstractmethod
    def node_count(self):
        """Número total de nodos en el subárbol."""
        pass


class NumNode(ASTNode):
    """Nodo hoja que representa un número literal."""

    def __init__(self, value):
        self.value = float(value) if "." in str(value) else int(value)

    def evaluate(self, env=None):
        return self.value

    def to_sexpr(self):
        return str(self.value)

    def to_dict(self):
        return {"type": "Literal", "value": self.value}

    def to_ascii_tree(self, indent="", is_last=True, use_ascii=False):
        marker = ("\\-- " if is_last else "+-- ") if use_ascii else ("└── " if is_last else "├── ")
        return [f"{indent}{marker}Num({self.value})"]

    def node_count(self):
        return 1

    def __repr__(self):
        return f"Num({self.value})"


class IdNode(ASTNode):
    """Nodo hoja que representa un identificador / variable."""

    def __init__(self, name):
        self.name = str(name)

    def evaluate(self, env=None):
        env = env or {}
        if self.name in env:
            return env[self.name]
        raise NameError(f"Variable '{self.name}' no definida")

    def to_sexpr(self):
        return self.name

    def to_dict(self):
        return {"type": "Identifier", "name": self.name}

    def to_ascii_tree(self, indent="", is_last=True, use_ascii=False):
        marker = ("\\-- " if is_last else "+-- ") if use_ascii else ("└── " if is_last else "├── ")
        return [f"{indent}{marker}Id({self.name})"]

    def node_count(self):
        return 1

    def __repr__(self):
        return f"Id({self.name})"


class BinaryOpNode(ASTNode):
    """Nodo interno que representa una operación binaria (operador como nodo)."""

    def __init__(self, op: str, left: ASTNode, right: ASTNode):
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self, env=None):
        l_val = self.left.evaluate(env)
        r_val = self.right.evaluate(env)
        if self.op == "+":
            return l_val + r_val
        elif self.op == "-":
            return l_val - r_val
        elif self.op == "*":
            return l_val * r_val
        elif self.op == "/":
            if r_val == 0:
                raise ZeroDivisionError("División por cero en AST")
            return l_val / r_val
        else:
            raise ValueError(f"Operador desconocido: {self.op}")

    def to_sexpr(self):
        return f"({self.op} {self.left.to_sexpr()} {self.right.to_sexpr()})"

    def to_tuple(self):
        """Representación en tuplas anidadas de Python."""
        def _tuple_repr(node):
            if isinstance(node, BinaryOpNode):
                return (node.op, _tuple_repr(node.left), _tuple_repr(node.right))
            elif isinstance(node, NumNode):
                return node.value
            elif isinstance(node, IdNode):
                return node.name
            return str(node)
        return _tuple_repr(self)

    def to_dict(self):
        return {
            "type": "BinaryExpression",
            "operator": self.op,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }

    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent)

    def to_ascii_tree(self, indent="", is_last=True, use_ascii=False):
        marker = ("\\-- " if is_last else "+-- ") if use_ascii else ("└── " if is_last else "├── ")
        lines = [f"{indent}{marker}Op({self.op})"]
        child_indent = indent + (("    " if is_last else "|   ") if use_ascii else ("    " if is_last else "│   "))

        lines.extend(self.left.to_ascii_tree(child_indent, is_last=False, use_ascii=use_ascii))
        lines.extend(self.right.to_ascii_tree(child_indent, is_last=True, use_ascii=use_ascii))
        return lines

    def node_count(self):
        return 1 + self.left.node_count() + self.right.node_count()

    def __repr__(self):
        return f"BinaryOp('{self.op}', {self.left}, {self.right})"


class NaryOpNode(ASTNode):
    """
    Forma alternativa de AST: Nodo N-Ario para operadores asociativos homogéneos.
    Ejemplo: en lugar de (+ (+ 3 4) 5), se compacta a (+ [3, 4, 5]).
    """

    def __init__(self, op: str, operands: list):
        self.op = op
        self.operands = operands

    def evaluate(self, env=None):
        if not self.operands:
            return 0
        vals = [op.evaluate(env) for op in self.operands]
        res = vals[0]
        for val in vals[1:]:
            if self.op == "+":
                res += val
            elif self.op == "*":
                res *= val
            elif self.op == "-":
                res -= val
            elif self.op == "/":
                res /= val
        return res

    def to_sexpr(self):
        ops_str = " ".join(op.to_sexpr() for op in self.operands)
        return f"({self.op} {ops_str})"

    def to_dict(self):
        return {
            "type": "NaryExpression",
            "operator": self.op,
            "operands": [op.to_dict() for op in self.operands],
        }

    def to_ascii_tree(self, indent="", is_last=True, use_ascii=False):
        marker = ("\\-- " if is_last else "+-- ") if use_ascii else ("└── " if is_last else "├── ")
        lines = [f"{indent}{marker}NaryOp({self.op})"]
        child_indent = indent + (("    " if is_last else "|   ") if use_ascii else ("    " if is_last else "│   "))
        for i, child in enumerate(self.operands):
            c_is_last = (i == len(self.operands) - 1)
            lines.extend(child.to_ascii_tree(child_indent, is_last=c_is_last, use_ascii=use_ascii))
        return lines

    def node_count(self):
        return 1 + sum(op.node_count() for op in self.operands)

    def __repr__(self):
        return f"NaryOp('{self.op}', {self.operands})"
