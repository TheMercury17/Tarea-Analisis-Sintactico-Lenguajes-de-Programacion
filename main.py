"""
================================================================================
Tarea Análisis Sintáctico | Lenguajes de Programación
Universidad Sergio Arboleda
Ciencias de la Computación e Inteligencia Artificial

Grupo 5:
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona

Puntos desarrollados:
1. Diapositiva 11/42: Implementación en ANTLR 4 (Target Python 3) y pruebas.
2. Diapositiva 12/42: Comprobación de las diferentes formas de AST vs Parse Tree.
3. Diapositiva 15/42: Implementación en ANTLR 4 y demostración de ambigüedad.
================================================================================
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Configurar rutas para importar módulos de cada subcarpeta
root_dir = os.path.dirname(os.path.abspath(__file__))
d11_dir = os.path.join(root_dir, "diapositiva_11")
d12_dir = os.path.join(root_dir, "diapositiva_12")
d15_dir = os.path.join(root_dir, "diapositiva_15")

for d in [root_dir, d11_dir, d12_dir, d15_dir]:
    if d not in sys.path:
        sys.path.insert(0, d)


def run_diapositiva_11():
    from diapositiva_11.test_diapositiva_11 import run_all_tests
    run_all_tests()


def run_diapositiva_12():
    from diapositiva_12.test_diapositiva_12 import run_all_ast_checks
    run_all_ast_checks()


def run_diapositiva_15():
    from diapositiva_15.test_ambiguedad import run_ambiguity_analysis
    run_ambiguity_analysis()


def run_all():
    print("\n" + "#" * 80)
    print("  EJECUTANDO SUITE COMPLETA DE ANÁLISIS SINTÁCTICO (DIAPOSITIVAS 11, 12 Y 15)")
    print("  GRUPO 5: Andrés Sebastián Coral Vallejo y Carol Arenas Cardona")
    print("#" * 80 + "\n")

    print("\n>>> INICIANDO PRUEBAS DE DIAPOSITIVA 11...\n")
    run_diapositiva_11()

    print("\n\n>>> INICIANDO COMPROBACIÓN DE FORMAS DE AST DE DIAPOSITIVA 12...\n")
    run_diapositiva_12()

    print("\n\n>>> INICIANDO PRUEBAS DE AMBIGÜEDAD DE DIAPOSITIVA 15...\n")
    run_diapositiva_15()

    print("\n" + "=" * 80)
    print("  ¡TODOS LOS ENTREGABLES FUERON EJECUTADOS CON ÉXITO!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ("11", "d11", "diapositiva_11"):
            run_diapositiva_11()
        elif arg in ("12", "d12", "diapositiva_12"):
            run_diapositiva_12()
        elif arg in ("15", "d15", "diapositiva_15"):
            run_diapositiva_15()
        elif arg in ("all", "--all", "-a"):
            run_all()
        else:
            print(f"Opción no reconocida: {arg}. Use: 11, 12, 15, o all")
    else:
        run_all()
