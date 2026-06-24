"""Parser da sintaxe da EasyAnsi.

Converte uma string com marcacao em uma lista de tokens. A logica e
totalmente independente de I/O e de codigos ANSI concretos (so consulta
``codes.resolve`` para validar nomes).

Sintaxe reconhecida:
- abertura:        ``//nome/``        ex.: ``//bold-blue/``
- fechamento:      ``/nome``          ex.: ``/bold-blue``
- fechamento curto:``//``             fecha a ultima tag aberta
- escape:          ``\\/`` e ``\\\\`` para imprimir ``/`` e ``\\`` literais

Regras de robustez (fail-safe): um nome desconhecido nunca quebra o texto;
o trecho e mantido literalmente. Por isso ``https://site`` ou caminhos como
``/pasta`` passam intactos.
"""

from __future__ import annotations

from typing import List, NamedTuple, Optional, Tuple

from . import codes


class Token(NamedTuple):
    """Unidade do texto ja interpretado.

    kind: 'text', 'open' ou 'close'.
    value: o texto (em 'text') ou o nome da tag (em 'open'/'close').
    codes: codigos ANSI resolvidos (apenas em 'open').
    """

    kind: str
    value: str
    codes: Tuple[str, ...] = ()


_NAME_CHARS = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#-"
)


def _read_name(text: str, start: int) -> Tuple[str, int]:
    """Le um nome de tag a partir de ``start``; devolve (nome, indice_final)."""
    j = start
    length = len(text)
    while j < length and text[j] in _NAME_CHARS:
        j += 1
    return text[start:j], j


def _try_open(text: str, i: int) -> Optional[Tuple[str, int]]:
    """Tenta casar uma abertura ``//nome/`` a partir do indice ``i``."""
    name, j = _read_name(text, i + 2)
    if not name:
        return None
    if j < len(text) and text[j] == "/" and codes.resolve(name) is not None:
        return name, j + 1
    return None


def _try_close(text: str, i: int) -> Optional[Tuple[str, int]]:
    """Tenta casar um fechamento explicito ``/nome`` a partir do indice ``i``."""
    name, j = _read_name(text, i + 1)
    if not name:
        return None
    if codes.resolve(name) is not None:
        return name, j
    return None


def parse(text: str) -> List[Token]:
    """Interpreta ``text`` e devolve a lista de tokens.

    Tags abertas e nao fechadas sao encerradas automaticamente no final.
    """
    tokens: List[Token] = []
    buffer: List[str] = []
    stack: List[str] = []
    i = 0
    length = len(text)

    def flush() -> None:
        if buffer:
            tokens.append(Token("text", "".join(buffer)))
            buffer.clear()

    while i < length:
        char = text[i]

        if char == "\\" and i + 1 < length and text[i + 1] in "/\\":
            buffer.append(text[i + 1])
            i += 2
            continue

        if char == "/":
            is_double = i + 1 < length and text[i + 1] == "/"

            if is_double:
                opened = _try_open(text, i)
                if opened is not None:
                    name, end = opened
                    resolved = codes.resolve(name) or []
                    flush()
                    tokens.append(Token("open", name, tuple(resolved)))
                    stack.append(name)
                    i = end
                    continue
                if stack:
                    flush()
                    tokens.append(Token("close", ""))
                    stack.pop()
                    i += 2
                    continue
                buffer.append("/")
                i += 1
                continue

            closed = _try_close(text, i)
            if closed is not None:
                name, end = closed
                if name in stack:
                    flush()
                    tokens.append(Token("close", name))
                    for j in range(len(stack) - 1, -1, -1):
                        if stack[j] == name:
                            del stack[j]
                            break
                    i = end
                    continue

            buffer.append("/")
            i += 1
            continue

        buffer.append(char)
        i += 1

    flush()
    for _ in stack:
        tokens.append(Token("close", ""))
    return tokens
