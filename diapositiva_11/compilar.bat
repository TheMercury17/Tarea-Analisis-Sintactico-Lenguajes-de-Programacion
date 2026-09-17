@echo off
echo ========================================================
echo Compilando gramatica ArithmeticExpr.g4 para Python 3...
echo ========================================================
antlr4 -Dlanguage=Python3 -visitor -listener ArithmeticExpr.g4
echo Compilacion finalizada exitosamente.
pause
