"""Geracao de titulos decorativos com linhas repetidas (sem I/O).

Responsavel apenas pelo layout visual: caractere, largura, alinhamento e
cores independentes para linhas e texto.
"""

from __future__ import annotations

import shutil
import sys
from typing import Literal, Optional

from . import codes, terminal
from .parser import parse
from .renderer import render

Align = Literal["center", "left"]


def _apply_style(text: str, style_name: Optional[str], *, use_color: bool) -> str:
    """Aplica um estilo ANSI ao texto; fail-safe se estilo invalido ou sem cor."""
    if not style_name or not use_color:
        return text
    resolved = codes.resolve(style_name)
    if not resolved:
        return text
    return f"{codes.sequence(resolved)}{text}{codes.RESET_SEQ}"


def _resolve_width(width: Optional[int]) -> int:
    """Obtem a largura do titulo; usa o terminal ou 80 como fallback."""
    if width is not None and width > 0:
        return width
    try:
        return shutil.get_terminal_size(fallback=(80, 24)).columns
    except (OSError, ValueError):
        return 80


def _fit_text(text: str, width: int) -> str:
    """Trunca texto longo para caber na largura disponivel."""
    if len(text) <= width:
        return text
    if width <= 3:
        return text[:width]
    return text[: width - 3] + "..."


def title(
    text: str,
    char: str = "=",
    *,
    width: Optional[int] = None,
    align: Align = "center",
    style: Optional[str] = None,
    text_style: Optional[str] = None,
    line_style: Optional[str] = None,
    color: Optional[bool] = None,
) -> str:
    """Monta um titulo com linhas decorativas acima e abaixo.

    Args:
        text: texto do titulo (aceita tags ``//cor/.../cor`` inline).
        char: caractere repetido nas linhas (ex.: ``=``, ``-``, ``~``).
        width: largura total das linhas; None usa a largura do terminal.
        align: ``"center"`` ou ``"left"``.
        style: estilo aplicado a linhas e ao texto.
        text_style: estilo apenas do texto do titulo.
        line_style: estilo apenas das linhas decorativas.
        color: força ligar/desligar a cor; None decide pelo terminal.

    Returns:
        String multilinha pronta para imprimir.
    """
    use_color = terminal.supports_color(sys.stdout) if color is None else color
    resolved_width = _resolve_width(width)
    line_char = char[:1] if char else "="

    plain_text = render(parse(text), color=False)
    plain_text = _fit_text(plain_text, resolved_width)

    resolved_line_style = line_style if line_style is not None else style
    resolved_text_style = text_style if text_style is not None else style

    line = line_char * resolved_width
    styled_line = _apply_style(line, resolved_line_style, use_color=use_color)

    if align == "center":
        title_line = plain_text.center(resolved_width)
    else:
        title_line = plain_text

    styled_title = _apply_style(title_line, resolved_text_style, use_color=use_color)

    return f"{styled_line}\n{styled_title}\n{styled_line}"


__all__ = ["title"]
