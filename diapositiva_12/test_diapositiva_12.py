"""
Comprobación y análisis de las diferentes formas de AST para la Diapositiva 12/42.
Expresión base de la diapositiva: "3 + 4 * 5"

Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
Asignatura: Lenguajes de Programación
"""

import sys
import os
import ast as python_ast

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importar dependencias de diapositiva 11 y locales
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
d11_dir = os.path.join(parent_dir, "diapositiva_11")
if d11_dir not in sys.path:
    sys.path.insert(0, d11_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from antlr4 import InputStream, CommonTokenStream
from ArithmeticExprLexer import ArithmeticExprLexer
from ArithmeticExprParser import ArithmeticExprParser
from tree_printer import format_tree_str
from ast_nodes import BinaryOpNode, NumNode, IdNode, NaryOpNode
from ast_builder import ASTBuilderVisitor, flatten_associative_ast


def count_cst_nodes(node):
    """Cuenta la cantidad total de nodos en el Parse Tree (CST)."""
    count = 1
    for i in range(node.getChildCount()):
        count += count_cst_nodes(node.getChild(i))
    return count


def analyze_expression_ast(expr_str: str):
    output_lines = []

    def log(msg=""):
        output_lines.append(msg)
        print(msg)

    log("=" * 80)
    log(f"  ANÁLISIS COMPARATIVO CST vs FORMAS DE AST PARA: '{expr_str}'")
    log("  Diapositiva 12/42 - Lenguajes de Programación")
    log("  Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona")
    log("=" * 80)

    # 1. Análisis Sintáctico con ANTLR (Generación del Parse Tree / CST)
    input_stream = InputStream(expr_str)
    lexer = ArithmeticExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArithmeticExprParser(token_stream)
    cst_tree = parser.program()

    total_cst_nodes = count_cst_nodes(cst_tree)

    log("\n[1] PARSE TREE (Árbol Sintáctico Concreto - CST) tal como en Diapositiva 12:")
    log("-------------------------------------------------------------------------")
    log("Conserva la totalidad de pasos de derivación de la gramática (E -> T -> F):")
    cst_str = format_tree_str(cst_tree, parser)
    log(cst_str)
    log(f"-> Total de nodos en el Parse Tree (CST): {total_cst_nodes} nodos")

    # 2. Construcción del AST mediante Visitor
    ast_builder = ASTBuilderVisitor()
    custom_ast = ast_builder.visit(cst_tree)
    total_ast_nodes = custom_ast.node_count()

    log("\n" + "=" * 80)
    log("[2] DIFERENTES FORMAS DE REPRESENTACIÓN DEL AST:")
    log("=" * 80)

    # Forma 1: AST Jerárquico Orientado a Objetos (POPO)
    log("\n>>> FORMA 1: AST Jerárquico Orientado a Objetos (Visual 2D / Clases)")
    log("    Los operadores son nodos internos; los operandos son nodos hoja.")
    log("    Se eliminan nodos de paso intermediarios (E, T, F) y puntuación innecesaria.")
    ast_tree_lines = custom_ast.to_ascii_tree()
    log("\n".join(ast_tree_lines))
    log(f"    -> Total de nodos en el AST: {total_ast_nodes} nodos (Reducción del {(1 - total_ast_nodes/total_cst_nodes)*100:.1f}%)")
    log(f"    -> Evaluación semántica del AST: {custom_ast.evaluate()}")

    # Forma 2: AST en Notación Prefija / S-Expressions y Tuplas Funcionales
    log("\n>>> FORMA 2: AST en Notación Prefija / S-Expressions (Estilo Lisp) y Tuplas")
    log("    Formato clásico en lenguajes funcionales e intérpretes teóricos:")
    log(f"    - S-Expression : {custom_ast.to_sexpr()}")
    log(f"    - Tuplas Python: {custom_ast.to_tuple()}")

    # Forma 3: AST Estructurado en Diccionario / JSON
    log("\n>>> FORMA 3: AST Estructurado en Diccionario / JSON (Estándar ESTree / Linters)")
    log("    Estructura serializable utilizada en herramientas modernas de análisis estático:")
    log(custom_ast.to_json(indent=2))

    # Forma 4: AST N-Ario / Compactado
    log("\n>>> FORMA 4: AST N-Ario Compactado (Operadores homogéneos agrupados)")
    flattened = flatten_associative_ast(custom_ast)
    log("    Representación en la que operaciones encadenadas se aplanan en un solo nodo:")
    log(f"    - S-Expression N-Aria: {flattened.to_sexpr()}")
    log("    - Árbol N-Ario:")
    log("\n".join(flattened.to_ascii_tree()))

    # Forma 5: Comparativa con el AST Nativo del compilador de Python
    log("\n>>> FORMA 5: AST Nativo del compilador de Python (Módulo 'ast')")
    log("    Representación que genera internamente CPython al compilar la misma expresión:")
    py_parsed = python_ast.parse(expr_str, mode="eval")
    log(f"    - ast.dump() estructurado:\n    {python_ast.dump(py_parsed, indent=2)}")

    return "\n".join(output_lines)


def run_all_ast_checks():
    # 1. Comprobación obligatoria: Caso de la Diapositiva 12 ("3 + 4 * 5")
    report_slide12 = analyze_expression_ast("3 + 4 * 5")

    # 2. Comprobación adicional: Caso con paréntesis "2 + 3 * (4 - 5)"
    print("\n\n" + "#" * 80)
    print("  CASO ADICIONAL 1: EXPRESIÓN CON PARÉNTESIS '2 + 3 * (4 - 5)'")
    print("#" * 80)
    report_extra1 = analyze_expression_ast("2 + 3 * (4 - 5)")

    # 3. Comprobación adicional: Caso asociativo encadenado "1 + 2 + 3 + 4"
    print("\n\n" + "#" * 80)
    print("  CASO ADICIONAL 2: CADENA ASOCIATIVA '1 + 2 + 3 + 4'")
    print("#" * 80)
    report_extra2 = analyze_expression_ast("1 + 2 + 3 + 4")

    # Guardar evidencia completa en archivo de texto
    evidencia_path = os.path.join(current_dir, "evidencia_formas_ast.txt")
    with open(evidencia_path, "w", encoding="utf-8") as f:
        f.write(report_slide12)
        f.write("\n\n" + "#" * 80 + "\n\n")
        f.write(report_extra1)
        f.write("\n\n" + "#" * 80 + "\n\n")
        f.write(report_extra2)

    print(f"\n[OK] Evidencia completa guardada en: {evidencia_path}")


if __name__ == "__main__":
    run_all_ast_checks()
