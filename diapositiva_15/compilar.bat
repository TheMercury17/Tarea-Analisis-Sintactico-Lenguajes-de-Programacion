@echo off
echo ========================================================
echo Compilando gramaticas de la diapositiva 15 para Python 3...
echo ========================================================
antlr4 -Dlanguage=Python3 -visitor -listener AmbiguousExpr.g4
antlr4 -Dlanguage=Python3 -visitor -listener AmbiguousExprReversed.g4
echo Compilacion finalizada exitosamente.
pause
