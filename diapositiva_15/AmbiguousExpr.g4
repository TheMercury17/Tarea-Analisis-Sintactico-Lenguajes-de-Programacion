// ============================================================================
// Autores: Grupo 5
// - Andrés Sebastián Coral Vallejo
// - Carol Arenas Cardona
// Asignatura: Lenguajes de Programación
// Diapositiva 15/42: Gramática ambigua de expresiones
// ============================================================================

grammar AmbiguousExpr;

// Regla inicial
program
    : expr EOF
    ;

// Regla ambigua de la diapositiva 15:
// E -> E + E
// E -> E * E
// E -> num
expr
    : expr '+' expr     # AddAmb
    | expr '*' expr     # MulAmb
    | NUM               # NumAmb
    ;

// Reglas léxicas
NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
