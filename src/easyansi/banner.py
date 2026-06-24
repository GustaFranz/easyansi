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

Align = Literal["centro", "esquerda"]


def _apply_style(text: str, style_name: Optional[str], *, use_color: bool) -> str:
    """Aplica um estilo ANSI ao texto; fail-safe se estilo invalido ou sem cor."""
    if not style_name or not use_color:
        return text
    resolved = codes.resolve(style_name)
    if not resolved:
        return text
    return f"{codes.sequence(resolved)}{text}{codes.RESET_SEQ}"


def _resolve_width(largura: Optional[int]) -> int:
    """Obtem a largura do titulo; usa o terminal ou 80 como fallback."""
    if largura is not None and largura > 0:
        return largura
    try:
        return shutil.get_terminal_size(fallback=(80, 24)).columns
    except (OSError, ValueError):
        return 80


def _fit_text(text: str, largura: int) -> str:
    """Trunca texto longo para caber na largura disponivel."""
    if len(text) <= largura:
        return text
    if largura <= 3:
        return text[:largura]
    return text[: largura - 3] + "..."


def titulo(
    text: str,
    char: str = "=",
    *,
    largura: Optional[int] = None,
    alinhar: Align = "centro",
    estilo: Optional[str] = None,
    estilo_texto: Optional[str] = None,
    estilo_linha: Optional[str] = None,
    color: Optional[bool] = None,
) -> str:
    """Monta um titulo com linhas decorativas acima e abaixo.

    Args:
        text: texto do titulo (aceita tags ``//cor/.../cor`` inline).
        char: caractere repetido nas linhas (ex.: ``=``, ``-``, ``~``).
        largura: largura total das linhas; None usa a largura do terminal.
        alinhar: ``"centro"`` ou ``"esquerda"``.
        estilo: estilo aplicado a linhas e ao texto.
        estilo_texto: estilo apenas do texto do titulo.
        estilo_linha: estilo apenas das linhas decorativas.
        color: força ligar/desligar a cor; None decide pelo terminal.

    Returns:
        String multilinha pronta para imprimir.
    """
    use_color = terminal.supports_color(sys.stdout) if color is None else color
    width = _resolve_width(largura)
    line_char = char[:1] if char else "="

    plain_text = render(parse(text), color=False)
    plain_text = _fit_text(plain_text, width)

    line_style = estilo_linha if estilo_linha is not None else estilo
    text_style = estilo_texto if estilo_texto is not None else estilo

    line = line_char * width
    styled_line = _apply_style(line, line_style, use_color=use_color)

    if alinhar == "centro":
        title_line = plain_text.center(width)
    else:
        title_line = plain_text

    styled_title = _apply_style(title_line, text_style, use_color=use_color)

    return f"{styled_line}\n{styled_title}\n{styled_line}"


__all__ = ["titulo"]
