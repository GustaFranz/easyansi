"""EasyAnsi - formatacao de strings no terminal de forma simples.

Sintaxe basica::

    from easyansi import eprint

    eprint("//bold-blue/Ola, mundo!/bold-blue")
    eprint("Sobrou //red/1/red item")

Tambem ha atalhos diretos (red, green, bold, ...) e mensagens prontas
(success, error, warning, info). O processamento ANSI no Windows e habilitado
automaticamente ao importar.
"""

from __future__ import annotations

from .activate import activate, deactivate, is_active
from .banner import titulo
from . import terminal
from .api import einput, eprint, fmt
from .preview import preview
from .shortcuts import (
    black,
    blue,
    bold,
    cyan,
    dim,
    error,
    green,
    info,
    italic,
    magenta,
    red,
    strike,
    style,
    success,
    underline,
    warning,
    white,
    yellow,
)
from .text import AnsiText, ansi, paint, perguntar

__version__ = "0.4.0"

__all__ = [
    "fmt",
    "eprint",
    "einput",
    "activate",
    "deactivate",
    "is_active",
    "preview",
    "ansi",
    "AnsiText",
    "titulo",
    "perguntar",
    "paint",
    "style",
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bold",
    "dim",
    "italic",
    "underline",
    "strike",
    "success",
    "error",
    "warning",
    "info",
    "__version__",
]

# Habilita sequencias ANSI no Windows assim que a biblioteca e importada.
terminal.enable_windows_ansi()
