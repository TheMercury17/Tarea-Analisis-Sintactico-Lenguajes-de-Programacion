"""
Demostración y pruebas empíricas de ambigüedad para la Diapositiva 15/42.
Gramática:
    E -> E + E
    E -> E * E
    E -> num

Cadena analizada: "2 + 3 * 4"

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

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
d11_dir = os.path.join(parent_dir, "diapositiva_11")
if d11_dir not in sys.path:
    sys.path.insert(0, d11_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode

# Gramática 15 directa (+ antes de *)
from AmbiguousExprLexer import AmbiguousExprLexer
from AmbiguousExprParser import AmbiguousExprParser

# Gramática 15 invertida (* antes de +)
from AmbiguousExprReversedLexer import AmbiguousExprReversedLexer
from AmbiguousExprReversedParser import AmbiguousExprReversedParser

# Gramática no ambigua de diapositiva 11
from ArithmeticExprLexer import ArithmeticExprLexer
from ArithmeticExprParser import ArithmeticExprParser
from evaluator import ArithmeticEvaluator

from evaluator_ambiguous import AmbiguousExprEvaluator, AmbiguousExprReversedEvaluator
from tree_printer import format_tree_str


def run_ambiguity_analysis():
    log_lines = []

    def log(msg=""):
        log_lines.append(msg)
        print(msg)

    log("=" * 80)
    log("  DEMOSTRACIÓN Y PRUEBAS DE AMBIGÜEDAD - DIAPOSITIVA 15/42")
    log("  Lenguajes de Programación - Universidad Sergio Arboleda")
    log("  Grupo 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona")
    log("=" * 80)

    cadena = "2 + 3 * 4"
    log(f"\nCadena de prueba analizada: '{cadena}'")

    # -------------------------------------------------------------------------
    # PARTE 1: DEMOSTRACIÓN TEÓRICA FORMAL
    # -------------------------------------------------------------------------
    log("\n" + "=" * 80)
    log("1. DEMOSTRACIÓN TEÓRICA FORMAL DE AMBIGÜEDAD")
    log("=" * 80)
    log("Definición: Una gramática independiente del contexto G es AMBIGUA si existe al")
    log("menos una cadena w en L(G) para la cual se pueden construir dos o más árboles")
    log("de derivación distintos (o dos derivaciones más a la izquierda distintas).")
    log("\nGramática de la Diapositiva 15:")
    log("    E -> E + E")
    log("    E -> E * E")
    log("    E -> num")

    log("\nPara la cadena '2 + 3 * 4', existen DOS derivaciones más a la izquierda válidas:")
    log("\n--- Derivación A (Prioridad a la Suma / Multiplicación en la raíz) ---")
    log("    E => E * E")
    log("      => (E + E) * E")
    log("      => (2 + E) * E")
    log("      => (2 + 3) * E")
    log("      => (2 + 3) * 4")
    log("    Árbol de Derivación A:")
    log("           E (*)")
    log("          /     \\")
    log("        E (+)    E (4)")
    log("       /     \\")
    log("     E (2)   E (3)")
    log("    Interpretación Semántica: (2 + 3) * 4 = 20")

    log("\n--- Derivación B (Prioridad a la Multiplicación / Suma en la raíz) ---")
    log("    E => E + E")
    log("      => 2 + E")
    log("      => 2 + (E * E)")
    log("      => 2 + (3 * E)")
    log("      => 2 + (3 * 4)")
    log("    Árbol de Derivación B:")
    log("           E (+)")
    log("          /     \\")
    log("     E (2)       E (*)")
    log("                /     \\")
    log("              E (3)   E (4)")
    log("    Interpretación Semántica: 2 + (3 * 4) = 14")

    log("\n>> Conclusión Teórica: La existencia de los Árboles A y B para la misma cadena")
    log("   demuestra matemática y formalmente que la gramática es AMBIGUA.")

    # -------------------------------------------------------------------------
    # PARTE 2: IMPLEMENTACIÓN EN ANTLR 4 Y COMPORTAMIENTO EMPÍRICO
    # -------------------------------------------------------------------------
    log("\n" + "=" * 80)
    log("2. IMPLEMENTACIÓN Y COMPROBACIÓN EN ANTLR 4")
    log("=" * 80)
    log("¿Qué hace ANTLR 4 cuando se le suministra una gramática formalmente ambigua?")
    log("ANTLR 4 no falla ni se detiene; en su lugar, aplica una heurística determinista:")
    log("1. Precedencia de regla (Alternative Precedence): la primera alternativa listada")
    log("   en el archivo .g4 tiene mayor precedencia.")
    log("2. Asociatividad por la izquierda por defecto.")

    # Experimento 1: AmbiguousExpr.g4 (+ listado primero)
    log("\n-------------------------------------------------------------------------")
    log("EXPERIMENTO 1: Gramática 'AmbiguousExpr.g4' (Regla '+' antes de '*')")
    log("-------------------------------------------------------------------------")
    lexer1 = AmbiguousExprLexer(InputStream(cadena))
    tokens1 = CommonTokenStream(lexer1)
    parser1 = AmbiguousExprParser(tokens1)
    tree1 = parser1.program()

    cst_str1 = format_tree_str(tree1, parser1)
    evaluator1 = AmbiguousExprEvaluator()
    val1 = evaluator1.visit(tree1)

    log("Parse Tree generado por ANTLR:")
    log(cst_str1)
    log(f"Representación en S-Expression: {tree1.toStringTree(recog=parser1)}")
    log(f"Valor numérico evaluado        : {val1}")
    log("Explicación: Dado que 'expr + expr' fue declarado primero en la regla, ANTLR")
    log("le otorgó prioridad a la suma, agrupando la expresión como (2 + 3) * 4 = 20.")
    log("¡Este resultado contradice la precedencia matemática estándar!")

    # Experimento 2: AmbiguousExprReversed.g4 (* listado primero)
    log("\n-------------------------------------------------------------------------")
    log("EXPERIMENTO 2: Gramática 'AmbiguousExprReversed.g4' (Regla '*' antes de '+')")
    log("-------------------------------------------------------------------------")
    lexer2 = AmbiguousExprReversedLexer(InputStream(cadena))
    tokens2 = CommonTokenStream(lexer2)
    parser2 = AmbiguousExprReversedParser(tokens2)
    tree2 = parser2.program()

    cst_str2 = format_tree_str(tree2, parser2)
    evaluator2 = AmbiguousExprReversedEvaluator()
    val2 = evaluator2.visit(tree2)

    log("Parse Tree generado por ANTLR:")
    log(cst_str2)
    log(f"Representación en S-Expression: {tree2.toStringTree(recog=parser2)}")
    log(f"Valor numérico evaluado        : {val2}")
    log("Explicación: Al simplemente intercambiar el orden físico de las dos líneas en")
    log("el archivo .g4, ANTLR cambia el árbol por completo a 2 + (3 * 4) = 14.")

    # -------------------------------------------------------------------------
    # PARTE 3: CONTRASTE CON LA GRAMÁTICA NO AMBIGUA DE LA DIAPOSITIVA 11
    # -------------------------------------------------------------------------
    log("\n" + "=" * 80)
    log("3. CONTRASTE: DESAMBIGUACIÓN ESTRUCTURAL (DIAPOSITIVA 11)")
    log("=" * 80)
    log("Para eliminar la ambigüedad en la teoría de compiladores, se estratifica la")
    log("gramática en niveles jerárquicos de no terminales (E para suma, T para producto,")
    log("F para factores atómicos):")
    log("    E -> E + T | T")
    log("    T -> T * F | F")
    log("    F -> num")

    lexer3 = ArithmeticExprLexer(InputStream(cadena))
    tokens3 = CommonTokenStream(lexer3)
    parser3 = ArithmeticExprParser(tokens3)
    tree3 = parser3.program()
    evaluator3 = ArithmeticEvaluator()
    val3 = evaluator3.visit(tree3)

    log(f"Resultado en la gramática de la Diapositiva 11: {val3}")
    log("El árbol producido es único e independiente del orden en que se listen las reglas,")
    log("porque la precedencia está codificada directamente en la estructura del lenguaje.")

    # -------------------------------------------------------------------------
    # PARTE 4: CUADRO COMPARATIVO RESUMEN
    # -------------------------------------------------------------------------
    log("\n" + "=" * 80)
    log("4. CUADRO COMPARATIVO FINAL: PRUEBA DE AMBIGÜEDAD")
    log("=" * 80)
    log(f"{'Configuración':<35} | {'Árbol / Agrupación':<20} | {'Resultado':<10} | {'¿Es Ambigua?'}")
    log("-" * 80)
    log(f"{'Teoría: Derivación A':<35} | {'((2 + 3) * 4)':<20} | {'20':<10} | {'SÍ (Árbol 1)'}")
    log(f"{'Teoría: Derivación B':<35} | {'(2 + (3 * 4))':<20} | {'14':<10} | {'SÍ (Árbol 2)'}")
    log(f"{'ANTLR: AmbiguousExpr (+ primero)':<35} | {'((2 + 3) * 4)':<20} | {'20':<10} | {'SÍ (Forzado por orden)'}")
    log(f"{'ANTLR: AmbiguousExprReversed (*)':<35} | {'(2 + (3 * 4))':<20} | {'14':<10} | {'SÍ (Forzado por orden)'}")
    log(f"{'Gramática Diapositiva 11 (E,T,F)':<35} | {'(2 + (3 * 4))':<20} | {'14':<10} | {'NO (Estratificada)'}")
    log("=" * 80)

    # Guardar en archivo de evidencia
    evidencia_file = os.path.join(current_dir, "evidencia_ambiguedad.txt")
    with open(evidencia_file, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    log(f"\n[OK] Evidencia de ambigüedad guardada exitosamente en:\n     {evidencia_file}")


if __name__ == "__main__":
    run_ambiguity_analysis()
