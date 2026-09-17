// ============================================================================
// Autores: Grupo 5
// - Andrés Sebastián Coral Vallejo
// - Carol Arenas Cardona
// Asignatura: Lenguajes de Programación
// Diapositiva 11/42: Gramática clásica para expresiones aritméticas
// ============================================================================

grammar ArithmeticExpr;

// Regla inicial que consume la expresión completa hasta el fin de archivo
program
    : expr EOF
    ;

// E -> E + T | E - T | T
// Asociatividad izquierda para operadores aditivos
expr
    : expr '+' term     # Add
    | expr '-' term     # Sub
    | term              # ToTerm
    ;

// T -> T * F | T / F | F
// Asociatividad izquierda y mayor precedencia para operadores multiplicativos
term
    : term '*' factor   # Mul
    | term '/' factor   # Div
    | factor            # ToFactor
    ;

// F -> id | num | ( E )
// Factores atómicos y expresiones entre paréntesis
factor
    : ID                # IdFactor
    | NUM               # NumFactor
    | '(' expr ')'      # ParenFactor
    ;

// ==================== Reglas Léxicas ====================

// Identificadores (nombres de variables)
ID  : [a-zA-Z_][a-zA-Z0-9_]* ;

// Números enteros o con punto flotante
NUM : [0-9]+ ('.' [0-9]+)? ;

// Espacios en blanco, tabulaciones y saltos de línea (se omiten)
WS  : [ \t\r\n]+ -> skip ;
