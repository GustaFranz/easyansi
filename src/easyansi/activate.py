"""Ativacao opt-in de print/input nativos com marcacao EasyAnsi.

Permite usar ``print()`` e ``input()`` normais apos ``activate()``, sem
renomear funcoes. ``deactivate()`` restaura os builtins originais.
"""

from __future__ import annotations

import builtins

from .api import einput, eprint

_builtin_print = builtins.print
_builtin_input = builtins.input
_active = False


def activate() -> None:
    """Substitui ``print`` e ``input`` globais pelas versoes coloridas da EasyAnsi.

    Idempotente: chamar varias vezes nao altera o estado apos a primeira ativacao.
    Use ``deactivate()`` para restaurar os builtins originais.
    """
    global _active
    if _active:
        return
    builtins.print = eprint
    builtins.input = einput
    _active = True


def deactivate() -> None:
    """Restaura ``print`` e ``input`` originais do Python."""
    global _active
    if not _active:
        return
    builtins.print = _builtin_print
    builtins.input = _builtin_input
    _active = False


def is_active() -> bool:
    """Indica se ``activate()`` esta em vigor."""
    return _active


__all__ = ["activate", "deactivate", "is_active"]
