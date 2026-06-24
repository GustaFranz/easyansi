"""Interface publica de alto nivel da EasyAnsi.

Funcoes principais que o usuario final utiliza no dia a dia. Esta camada
apenas orquestra parser, renderer e terminal (baixo acoplamento) e mantem
``print``/``input`` nativos intactos.
"""

from __future__ import annotations

import builtins
import sys
from typing import IO, Any, Optional

from . import terminal
from .parser import parse
from .renderer import render

_builtin_print = builtins.print
_builtin_input = builtins.input


def fmt(text: str, *, color: Optional[bool] = None) -> str:
    """Formata uma string com marcacao da EasyAnsi e retorna o resultado.

    Args:
        text: texto com tags, ex.: ``"//bold-blue/Ola/bold-blue"``.
        color: força ligar (True) ou desligar (False) a cor. Se None,
            decide automaticamente conforme o terminal.

    Returns:
        A string formatada (com ANSI) ou limpa, pronta para imprimir.
    """
    use_color = terminal.supports_color(sys.stdout) if color is None else color
    return render(parse(text), color=use_color)


def eprint(
    *values: Any,
    sep: str = " ",
    end: str = "\n",
    file: Optional[IO[str]] = None,
    color: Optional[bool] = None,
    flush: bool = False,
) -> None:
    """Versao colorida de ``print``.

    Aceita os mesmos parametros de ``print`` (sep, end, file, flush). Apenas
    argumentos ``str`` passam pela marcacao; outros tipos sao convertidos com
    ``str()`` normalmente.

    Args:
        color: força ligar/desligar a cor; None decide pelo destino.
    """
    stream = sys.stdout if file is None else file
    use_color = terminal.supports_color(stream) if color is None else color
    rendered = [
        render(parse(value), color=use_color) if isinstance(value, str) else str(value)
        for value in values
    ]
    _builtin_print(sep.join(rendered), end=end, file=stream, flush=flush)


def einput(prompt: str = "", *, color: Optional[bool] = None) -> str:
    """Versao colorida de ``input``: aceita marcacao no texto do prompt.

    Args:
        prompt: texto do prompt, podendo conter tags da EasyAnsi.
        color: força ligar/desligar a cor; None decide pelo terminal.

    Returns:
        A linha digitada pelo usuario.
    """
    use_color = terminal.supports_color(sys.stdout) if color is None else color
    return _builtin_input(render(parse(prompt), color=use_color))
