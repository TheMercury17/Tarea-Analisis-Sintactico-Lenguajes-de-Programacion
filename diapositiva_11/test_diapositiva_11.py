"""
Suite de pruebas automatizadas para la Diapositiva 11/42.
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
Asignatura: Lenguajes de Programación
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Asegurar que se pueda importar el paquete local
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from antlr4 import InputStream, CommonTokenStream
from ArithmeticExprLexer import ArithmeticExprLexer
from ArithmeticExprParser import ArithmeticExprParser
from evaluator import ArithmeticEvaluator
from error_listener import VerboseErrorListener
from tree_printer import format_tree_str


def parse_and_evaluate(expr_str: str, symbol_table=None):
    """
    Parsea una expresión con ANTLR4 y la evalúa usando el Visitor.
    Retorna un diccionario con el estado, valor, errores y árbol sintáctico.
    """
    input_stream = InputStream(expr_str)
    lexer = ArithmeticExprLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_error_listener = VerboseErrorListener()
    lexer.addErrorListener(lexer_error_listener)

    token_stream = CommonTokenStream(lexer)
    parser = ArithmeticExprParser(token_stream)
    parser.removeErrorListeners()
    parser_error_listener = VerboseErrorListener()
    parser.addErrorListener(parser_error_listener)

    tree = parser.program()
    all_errors = lexer_error_listener.errors + parser_error_listener.errors

    if all_errors:
        return {
            "success": False,
            "errors": all_errors,
            "value": None,
            "tree_str": None,
        }

    evaluator = ArithmeticEvaluator(symbol_table=symbol_table)
    try:
        val = evaluator.visit(tree)
        tree_str = format_tree_str(tree, parser)
        return {
            "success": True,
            "errors": [],
            "value": val,
            "tree_str": tree_str,
        }
    except Exception as e:
        return {
            "success": False,
            "errors": [str(e)],
            "value": None,
            "tree_str": None,
        }


def run_all_tests():
    print("=" * 80)
    print("  PRUEBAS DIAPOSITIVA 11/42 - GRAMÁTICA CLÁSICA DE EXPRESIONES ARITMÉTICAS")
    print("  Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona")
    print("=" * 80)

    # 1. Casos explícitos de la diapositiva 11
    slide_cases = [
        ("2 + 3 * 4", 14, "Ejemplo 1 de la diapositiva: precedencia de * sobre +"),
        ("2 + 3 - 4", 1, "Ejemplo 2 de la diapositiva: asociatividad izquierda de + y -"),
        ("2 + 3 * (4 - 5)", -1, "Ejemplo 3 de la diapositiva: alteración de precedencia con paréntesis"),
    ]

    print("\n[FASE 1] Casos de prueba directos de la Diapositiva 11:")
    for expr, expected, desc in slide_cases:
        res = parse_and_evaluate(expr)
        status = "PASÓ" if res["success"] and res["value"] == expected else "FALLÓ"
        print(f"  Expresión : {expr}")
        print(f"  Descripción: {desc}")
        print(f"  Resultado : {res['value']} (Esperado: {expected}) -> [{status}]")
        assert res["success"] and res["value"] == expected, f"Fallo en {expr}"
        print()

    # 2. Casos con variables (id)
    print("[FASE 2] Casos con identificadores (F -> id):")
    vars_dict = {"x": 10, "y": 5, "z": 2, "base": 100}
    var_cases = [
        ("x + y * z", 20, "x=10, y=5, z=2 -> 10 + (5*2) = 20"),
        ("(x + y) * z", 30, "(10 + 5) * 2 = 30"),
        ("base - x * y", 50, "100 - (10 * 5) = 50"),
    ]
    for expr, expected, desc in var_cases:
        res = parse_and_evaluate(expr, symbol_table=vars_dict)
        status = "PASÓ" if res["success"] and res["value"] == expected else "FALLÓ"
        print(f"  Expresión : {expr}")
        print(f"  Descripción: {desc}")
        print(f"  Resultado : {res['value']} (Esperado: {expected}) -> [{status}]")
        assert res["success"] and res["value"] == expected, f"Fallo en {expr}"
        print()

    # 3. Casos de asociatividad izquierda encadenada
    print("[FASE 3] Pruebas de asociatividad izquierda:")
    assoc_cases = [
        ("10 - 3 - 2", 5, "10 - 3 - 2 debe evaluarse como (10 - 3) - 2 = 5, no 10 - (3 - 2) = 9"),
        ("24 / 4 / 2", 3.0, "24 / 4 / 2 debe ser (24 / 4) / 2 = 3.0, no 24 / (4 / 2) = 12.0"),
    ]
    for expr, expected, desc in assoc_cases:
        res = parse_and_evaluate(expr)
        status = "PASÓ" if res["success"] and res["value"] == expected else "FALLÓ"
        print(f"  Expresión : {expr}")
        print(f"  Resultado : {res['value']} (Esperado: {expected}) -> [{status}]")
        assert res["success"] and res["value"] == expected, f"Fallo en {expr}"
        print()

    # 4. Casos sintácticamente inválidos
    print("[FASE 4] Detección de errores sintácticos:")
    invalid_cases = [
        ("2 + * 3", "Operador consecutivo no válido"),
        ("(2 + 3", "Paréntesis sin cerrar"),
        ("+ 5", "Falta operando izquierdo"),
        ("2 3", "Falta operador entre operandos"),
    ]
    for expr, desc in invalid_cases:
        res = parse_and_evaluate(expr)
        status = "PASÓ (Rechazado correctamente)" if not res["success"] else "FALLÓ (Fue aceptado erróneamente)"
        print(f"  Expresión : {expr}")
        print(f"  Motivo     : {desc}")
        print(f"  Errores   : {res['errors']}")
        print(f"  Estado    : [{status}]\n")
        assert not res["success"], f"Expresión inválida '{expr}' fue aceptada."

    # 5. Visualización del árbol para el ejemplo 1
    print("[FASE 5] Árbol de análisis sintáctico (Parse Tree) para '2 + 3 * 4':")
    res_tree = parse_and_evaluate("2 + 3 * 4")
    print(res_tree["tree_str"])
    print("\n" + "=" * 80)
    print("  TODAS LAS PRUEBAS DE LA DIAPOSITIVA 11 PASARON EXITOSAMENTE")
    print("=" * 80)


if __name__ == "__main__":
    run_all_tests()
