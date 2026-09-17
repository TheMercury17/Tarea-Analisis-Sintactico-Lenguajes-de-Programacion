"""
Impresor de árboles sintácticos en formato texto/ASCII.
Autores: Grupo 5
- Andrés Sebastián Coral Vallejo
- Carol Arenas Cardona
"""

import sys
from antlr4.tree.Tree import TerminalNodeImpl

# Asegurar salida utf-8 en consolas Windows si es posible
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def print_ascii_tree(node, rule_names, indent="", is_last=True, use_ascii=False):
    lines = []
    if use_ascii:
        marker = "\\-- " if is_last else "+-- "
    else:
        marker = "└── " if is_last else "├── "

    if isinstance(node, TerminalNodeImpl):
        text = node.getText()
        if text != "<EOF>":
            lines.append(f"{indent}{marker}Terminal: '{text}'")
    else:
        rule_idx = node.getRuleIndex()
        rule_name = rule_names[rule_idx] if rule_idx < len(rule_names) else f"rule_{rule_idx}"
        lines.append(f"{indent}{marker}{rule_name}")

        child_count = node.getChildCount()
        for i in range(child_count):
            child = node.getChild(i)
            # Omitir EOF en la visualización
            if isinstance(child, TerminalNodeImpl) and child.getText() == "<EOF>":
                continue
            child_is_last = (i == child_count - 1) or (
                i == child_count - 2
                and isinstance(node.getChild(child_count - 1), TerminalNodeImpl)
                and node.getChild(child_count - 1).getText() == "<EOF>"
            )
            if use_ascii:
                child_indent = indent + ("    " if is_last else "|   ")
            else:
                child_indent = indent + ("    " if is_last else "│   ")
            lines.extend(print_ascii_tree(child, rule_names, child_indent, child_is_last, use_ascii=use_ascii))

    return lines


def format_tree_str(tree, parser, use_ascii=False):
    lines = print_ascii_tree(tree, parser.ruleNames, indent="", is_last=True, use_ascii=use_ascii)
    return "\n".join(lines)
