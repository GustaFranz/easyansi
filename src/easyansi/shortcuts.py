"""Atalhos de alto nivel: funcoes diretas de cor/estilo e mensagens prontas.

Pensado para quem quer praticidade maxima e bom autocomplete no editor, sem
precisar lembrar da sintaxe ``//cor/.../cor``. Tudo aqui e fail-safe: se a
saida nao suportar cor, devolve o texto puro.
"""

from __future__ import annotations

import sys
from typing import Any, IO, Optional

from . import codes, terminal


def _wrap(name: str, text: str, color: Optional[bool]) -> str:
    """Envolve ``text`` com o estilo ``name`` (ex.: 'red', 'bold-blue')."""
    use_color = terminal.supports_color(sys.stdout) if color is None else color
    resolved = codes.resolve(name)
    if not use_color or not resolved:
        return text
    return f"{codes.sequence(resolved)}{text}{codes.RESET_SEQ}"


# --- Cores de texto -------------------------------------------------------

def black(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto preto."""
    return _wrap("black", text, color)


def red(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto vermelho."""
    return _wrap("red", text, color)


def green(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto verde."""
    return _wrap("green", text, color)


def yellow(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto amarelo."""
    return _wrap("yellow", text, color)


def blue(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto azul."""
    return _wrap("blue", text, color)


def magenta(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto magenta."""
    return _wrap("magenta", text, color)


def cyan(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto ciano."""
    return _wrap("cyan", text, color)


def white(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto branco."""
    return _wrap("white", text, color)


# --- Estilos --------------------------------------------------------------

def bold(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto em negrito."""
    return _wrap("bold", text, color)


def dim(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto esmaecido (dim)."""
    return _wrap("dim", text, color)


def italic(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto em italico."""
    return _wrap("italic", text, color)


def underline(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto sublinhado."""
    return _wrap("underline", text, color)


def strike(text: str, *, color: Optional[bool] = None) -> str:
    """Deixa o texto tachado."""
    return _wrap("strike", text, color)


def style(name: str, text: str, *, color: Optional[bool] = None) -> str:
    """Aplica qualquer combinacao de estilo pelo nome.

    Args:
        name: nome do estilo, ex.: 'bold-blue', 'bg-amarelo', '#ff8800'.
        text: texto a formatar.
        color: força ligar/desligar a cor; None decide pelo terminal.
    """
    return _wrap(name, text, color)


# --- Mensagens de status prontas -----------------------------------------

def _safe_symbol(unicode_symbol: str, ascii_symbol: str, stream: IO[str]) -> str:
    """Usa o simbolo Unicode se o terminal suportar; senao, o equivalente ASCII."""
    encoding = getattr(stream, "encoding", None) or "utf-8"
    try:
        unicode_symbol.encode(encoding)
        return unicode_symbol
    except (UnicodeEncodeError, LookupError):
        return ascii_symbol


def _status(
    values: tuple,
    color_name: str,
    unicode_symbol: str,
    ascii_symbol: str,
    sep: str,
    end: str,
    file: Optional[IO[str]],
) -> None:
    stream = sys.stdout if file is None else file
    symbol = _safe_symbol(unicode_symbol, ascii_symbol, stream)
    text = sep.join(str(v) for v in values)
    message = f"{symbol} {text}" if symbol else text
    if terminal.supports_color(stream):
        resolved = codes.resolve(color_name) or []
        message = f"{codes.sequence(resolved)}{message}{codes.RESET_SEQ}"
    print(message, end=end, file=stream)


def success(*values: Any, sep: str = " ", end: str = "\n", file: Optional[IO[str]] = None) -> None:
    """Imprime uma mensagem de sucesso (verde, prefixo de check)."""
    _status(values, "green", "\u2713", "[OK]", sep, end, file)


def error(*values: Any, sep: str = " ", end: str = "\n", file: Optional[IO[str]] = None) -> None:
    """Imprime uma mensagem de erro (vermelho, prefixo de X)."""
    _status(values, "red", "\u2717", "[ERRO]", sep, end, file)


def warning(*values: Any, sep: str = " ", end: str = "\n", file: Optional[IO[str]] = None) -> None:
    """Imprime um aviso (amarelo, prefixo de exclamacao)."""
    _status(values, "yellow", "\u26a0", "[!]", sep, end, file)


def info(*values: Any, sep: str = " ", end: str = "\n", file: Optional[IO[str]] = None) -> None:
    """Imprime uma informacao (azul/ciano, prefixo de i)."""
    _status(values, "cyan", "\u2139", "[i]", sep, end, file)
