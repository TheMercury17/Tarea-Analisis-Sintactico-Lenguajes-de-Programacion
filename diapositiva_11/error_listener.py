"""
Manejador de errores sintácticos personalizado para ANTLR4.
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
"""

from antlr4.error.ErrorListener import ErrorListener


class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Línea {line}:{column} - {msg}"
        self.errors.append(error_msg)

    def has_errors(self):
        return len(self.errors) > 0
