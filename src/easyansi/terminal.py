"""Deteccao de ambiente e suporte a cor (isolado do resto da biblioteca).

Responsabilidades:
- decidir se a saida deve ou nao receber codigos ANSI;
- habilitar o modo VT (sequencias ANSI) no Windows.
"""

from __future__ import annotations

import os
import sys
from typing import IO, Optional

_windows_ansi_enabled = False


def supports_color(stream: Optional[IO[str]] = None) -> bool:
    """Indica se devemos emitir codigos ANSI para o stream informado.

    Regras (do mais forte para o mais fraco):
    - FORCE_COLOR definido  -> sempre True;
    - NO_COLOR definido      -> sempre False (padrao no-color.org);
    - TERM == 'dumb'         -> False;
    - stream sem TTY         -> False (arquivo, pipe, redirecionamento).

    Args:
        stream: fluxo de saida (padrao: sys.stdout).

    Returns:
        True se cor deve ser aplicada, False caso contrario.
    """
    if stream is None:
        stream = sys.stdout

    if os.environ.get("FORCE_COLOR"):
        return True
    if "NO_COLOR" in os.environ:
        return False
    if os.environ.get("TERM") == "dumb":
        return False

    try:
        is_tty = stream.isatty()
    except (AttributeError, ValueError):
        return False
    return bool(is_tty)


def enable_windows_ansi() -> bool:
    """Habilita o processamento de sequencias ANSI no console do Windows.

    Em sistemas nao-Windows e um no-op que retorna True. Idempotente.

    Returns:
        True se o terminal suporta/aceitou ANSI, False caso contrario.
    """
    global _windows_ansi_enabled

    if sys.platform != "win32":
        return True
    if _windows_ansi_enabled:
        return True

    try:
        import ctypes
        from ctypes import wintypes

        kernel32 = ctypes.windll.kernel32
        enable_vt = 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING

        for handle_id in (-11, -12):  # STDOUT, STDERR
            handle = kernel32.GetStdHandle(handle_id)
            if handle in (0, -1):
                continue
            mode = wintypes.DWORD()
            if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                continue
            kernel32.SetConsoleMode(handle, mode.value | enable_vt)

        _windows_ansi_enabled = True
        return True
    except Exception:
        return False
