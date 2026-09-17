// ============================================================================
// Autores: Grupo 5
// - Andrés Sebastián Coral Vallejo
// - Carol Arenas Cardona
// Asignatura: Lenguajes de Programación
// Diapositiva 15/42: Gramática ambigua con orden de alternativas invertido
// ============================================================================

grammar AmbiguousExprReversed;

program
    : expr EOF
    ;

// En esta versión, '*' se define ANTES de '+'
expr
    : expr '*' expr     # MulAmbRev
    | expr '+' expr     # AddAmbRev
    | NUM               # NumAmbRev
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
