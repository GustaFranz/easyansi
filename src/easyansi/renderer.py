"""Renderizador: transforma tokens em texto final.

Com ``color=True`` gera a string com sequencias ANSI; com ``color=False``
devolve apenas o texto limpo (util para arquivos, pipes e export futuro).
"""

from __future__ import annotations

from typing import List, Tuple

from . import codes
from .parser import Token


def render(tokens: List[Token], color: bool = True) -> str:
    """Converte uma lista de tokens em string.

    No fechamento de uma tag, emite um reset e reaplica os estilos das tags
    ainda abertas, garantindo aninhamento correto. Ex.: em
    ``//red/a //bold/b/bold c/red`` o trecho ``c`` continua vermelho.

    Args:
        tokens: lista produzida por ``parser.parse``.
        color: se False, ignora a formatacao e retorna apenas o texto.

    Returns:
        A string final, com ou sem codigos ANSI.
    """
    out: List[str] = []
    open_stack: List[Tuple[str, ...]] = []

    for token in tokens:
        if token.kind == "text":
            out.append(token.value)
        elif token.kind == "open":
            open_stack.append(token.codes)
            if color and token.codes:
                out.append(codes.sequence(list(token.codes)))
        elif token.kind == "close":
            if open_stack:
                open_stack.pop()
            if color:
                out.append(codes.RESET_SEQ)
                for active in open_stack:
                    if active:
                        out.append(codes.sequence(list(active)))

    return "".join(out)
