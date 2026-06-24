"""Wrapper fluente para colorir texto inteiro e titulos decorativos.

Fornece ``AnsiText`` e a factory ``ansi()`` para encadeamento de estilos
com escopos distintos em ``print`` e ``input``.
"""

from __future__ import annotations

import builtins
from typing import Any, Literal, Optional

from . import terminal
from .banner import title as format_title
from .banner import _apply_style
from .parser import parse
from .renderer import render
from .shortcuts import style

Scope = Literal["text", "prompt", "answer", "both"]

_builtin_input = builtins.input


class AnsiText:
    """Texto envolvido para formatacao fluente da EasyAnsi."""

    def __init__(self, text: str) -> None:
        self._text = text
        self._text_style: Optional[str] = None
        self._prompt_style: Optional[str] = None
        self._answer_style: Optional[str] = None
        self._banner: Optional[dict[str, Any]] = None

    def easyansi(self, style: str, *, scope: Scope = "text") -> AnsiText:
        """Define estilo ANSI; ``scope`` controla onde aplica em ``read()``/``print()``."""
        if scope == "text":
            self._text_style = style
        elif scope == "prompt":
            self._prompt_style = style
        elif scope == "answer":
            self._answer_style = style
        elif scope == "both":
            self._prompt_style = style
            self._answer_style = style
        return self

    def title(
        self,
        char: str = "=",
        *,
        width: Optional[int] = None,
        align: Literal["center", "left"] = "center",
        style: Optional[str] = None,
        text_style: Optional[str] = None,
        line_style: Optional[str] = None,
    ) -> AnsiText:
        """Configura saida como titulo decorativo com linhas repetidas."""
        self._banner = {
            "char": char,
            "width": width,
            "align": align,
            "style": style,
            "text_style": text_style,
            "line_style": line_style,
        }
        return self

    def render(self, *, color: Optional[bool] = None) -> str:
        """Retorna a string formatada para uso em ``print``/``eprint``."""
        import sys

        use_color = terminal.supports_color(sys.stdout) if color is None else color

        if self._banner is not None:
            return format_title(
                self._text,
                self._banner["char"],
                width=self._banner["width"],
                align=self._banner["align"],
                style=self._banner["style"],
                text_style=self._banner["text_style"],
                line_style=self._banner["line_style"],
                color=use_color,
            )

        inner = render(parse(self._text), color=use_color)
        return _apply_style(inner, self._text_style, use_color=use_color)

    def read(self, *, color: Optional[bool] = None) -> str:
        """Leitura interativa: estiliza prompt e/ou resposta conforme escopos."""
        import sys

        use_color = terminal.supports_color(sys.stdout) if color is None else color
        prompt_style = self._prompt_style or self._text_style
        prompt_inner = render(parse(self._text), color=use_color)
        styled_prompt = _apply_style(prompt_inner, prompt_style, use_color=use_color)
        answer = _builtin_input(styled_prompt)
        return _apply_style(answer, self._answer_style, use_color=use_color)

    def print(
        self,
        *,
        end: str = "\n",
        file: Optional[Any] = None,
        color: Optional[bool] = None,
        flush: bool = False,
    ) -> None:
        """Imprime o texto formatado via ``eprint``."""
        from .api import eprint

        eprint(self, end=end, file=file, color=color, flush=flush)

    def __str__(self) -> str:
        return self.render()


def ansi(text: str) -> AnsiText:
    """Cria um wrapper fluente para formatar texto inteiro ou titulos."""
    return AnsiText(text)


def ask(
    text: str,
    *,
    prompt_style: Optional[str] = None,
    answer_style: Optional[str] = None,
    color: Optional[bool] = None,
) -> str:
    """Pergunta ao usuario com estilos opcionais no prompt e na resposta.

    Args:
        text: texto da pergunta.
        prompt_style: estilo do prompt (ex.: ``"bold-blue"``).
        answer_style: estilo aplicado ao valor retornado (ex.: ``"green"``).
        color: força ligar/desligar a cor; None decide pelo terminal.

    Returns:
        A linha digitada pelo usuario, opcionalmente com ANSI na resposta.
    """
    wrapper = ansi(text)
    if prompt_style:
        wrapper.easyansi(prompt_style, scope="prompt")
    if answer_style:
        wrapper.easyansi(answer_style, scope="answer")
    return wrapper.read(color=color)


def paint(text: str, style_name: str, *, color: Optional[bool] = None) -> str:
    """Aplica estilo ao texto inteiro (ordem: texto, estilo)."""
    return style(style_name, text, color=color)


__all__ = ["AnsiText", "ansi", "ask", "paint"]
