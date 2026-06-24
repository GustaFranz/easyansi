"""Integracao com o modulo ``logging`` padrao do Python.

Responsabilidade unica: formatar registros de log com cores no terminal,
reutilizando ``codes``, ``terminal`` e ``api.fmt``. Import explicito::

    from easyansi.logging import ColorFormatter, setup_logging
"""

from __future__ import annotations

import logging
import sys
from copy import copy
from typing import Dict, IO, Mapping, Optional, Union

from . import codes, terminal
from .api import fmt

DEFAULT_LEVEL_COLORS: Dict[int, str] = {
    logging.DEBUG: "dim",
    logging.INFO: "cyan",
    logging.WARNING: "yellow",
    logging.ERROR: "red",
    logging.CRITICAL: "bold-red",
}

DEFAULT_LOG_FORMAT = "%(levelname)s | %(message)s"


class ColorFormatter(logging.Formatter):
    """Formatter que colore o nome do nivel de log no terminal.

    Respeita ``NO_COLOR``, saida nao-TTY e ``FORCE_COLOR`` via
    ``terminal.supports_color``. Com ``markup=True``, a mensagem passa pela
    sintaxe da EasyAnsi (``//cor/.../cor``) antes de montar a linha.

    Args:
        fmt: layout da linha (padrao logging).
        datefmt: formato de data/hora opcional.
        color: forca ligar/desligar cor; None decide pelo stream.
        markup: se True, interpreta marcacao EasyAnsi na mensagem.
        level_colors: mapa ``nivel (int) -> estilo`` EasyAnsi.
        stream: fluxo de saida usado para detectar suporte a cor.
    """

    def __init__(
        self,
        fmt: str = DEFAULT_LOG_FORMAT,
        datefmt: Optional[str] = None,
        *,
        color: Optional[bool] = None,
        markup: bool = False,
        level_colors: Optional[Mapping[int, str]] = None,
        stream: Optional[IO[str]] = None,
    ) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt)
        self.color = color
        self.markup = markup
        self.level_colors = dict(level_colors or DEFAULT_LEVEL_COLORS)
        self.stream = sys.stderr if stream is None else stream

    def _use_color(self) -> bool:
        """Decide se a formatacao deve incluir codigos ANSI."""
        if self.color is None:
            return terminal.supports_color(self.stream)
        return self.color

    def _colorize_level(self, line: str, level_name: str, level_no: int) -> str:
        """Aplica cor apenas ao nome do nivel na linha formatada."""
        style = self.level_colors.get(level_no)
        if not style:
            return line
        resolved = codes.resolve(style)
        if not resolved:
            return line
        colored = f"{codes.sequence(resolved)}{level_name}{codes.RESET_SEQ}"
        return line.replace(level_name, colored, 1)

    def format(self, record: logging.LogRecord) -> str:
        """Formata um registro de log, colorindo o nivel quando aplicavel."""
        use_color = self._use_color()
        work = record

        if self.markup:
            work = copy(record)
            work.msg = fmt(record.getMessage(), color=use_color)
            work.args = ()

        line = super().format(work)

        if not use_color:
            return line

        return self._colorize_level(line, work.levelname, work.levelno)


def setup_logging(
    level: Union[int, str] = logging.INFO,
    fmt: str = DEFAULT_LOG_FORMAT,
    datefmt: Optional[str] = None,
    *,
    markup: bool = False,
    color: Optional[bool] = None,
    stream: Optional[IO[str]] = None,
    force: bool = False,
) -> None:
    """Configura o logging raiz com ``ColorFormatter`` em um ``StreamHandler``.

    Equivalente pratico a ``logging.basicConfig`` com cores. Por padrao nao
    reconfigura se handlers ja existirem (``force=False``).

    Args:
        level: nivel minimo de log (ex.: ``logging.INFO``).
        fmt: layout da linha.
        datefmt: formato de data/hora opcional.
        markup: interpreta marcacao EasyAnsi nas mensagens.
        color: forca ligar/desligar cor; None decide pelo stream.
        stream: saida (padrao: ``sys.stderr``, como no logging padrao).
        force: se True, reconfigura mesmo com handlers existentes.
    """
    out = sys.stderr if stream is None else stream
    handler = logging.StreamHandler(out)
    handler.setFormatter(
        ColorFormatter(
            fmt=fmt,
            datefmt=datefmt,
            color=color,
            markup=markup,
            stream=out,
        )
    )
    logging.basicConfig(level=level, handlers=[handler], force=force)


__all__ = ["ColorFormatter", "DEFAULT_LEVEL_COLORS", "DEFAULT_LOG_FORMAT", "setup_logging"]
