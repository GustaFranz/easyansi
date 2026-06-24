"""Descoberta visual: mostra no terminal os estilos e cores disponiveis.

Rode ``easyansi.preview()`` uma vez para conhecer toda a paleta sem precisar
abrir a documentacao. Pensado tambem para quem aprende melhor vendo do que
lendo (apoio a acessibilidade).
"""

from __future__ import annotations

import sys
from typing import IO, Optional

from . import codes, terminal

_BASE_COLORS = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
_STYLE_NAMES = ["bold", "dim", "italic", "underline", "strike"]


def _swatch(name: str, label: str, use_color: bool) -> str:
    resolved = codes.resolve(name)
    if not use_color or not resolved:
        return label
    return f"{codes.sequence(resolved)}{label}{codes.RESET_SEQ}"


def preview(file: Optional[IO[str]] = None) -> None:
    """Imprime uma tabela com estilos e cores reconhecidos pela EasyAnsi.

    Args:
        file: stream de saida (padrao: sys.stdout).
    """
    stream = sys.stdout if file is None else file
    use_color = terminal.supports_color(stream)

    def line(text: str = "") -> None:
        print(text, file=stream)

    line(_swatch("bold", "EasyAnsi - paleta disponivel", use_color))
    line()

    line("Estilos:")
    for name in _STYLE_NAMES:
        sample = _swatch(name, f"  exemplo //{name}/", use_color)
        line(f"{sample}  ->  use: //{name}/texto/{name}")
    line()

    line("Cores (texto / brilhante / fundo):")
    for name in _BASE_COLORS:
        fg = _swatch(name, f"{name:<9}", use_color)
        bright = _swatch(f"bright-{name}", "brilhante", use_color)
        bg = _swatch(f"bg-{name}", " fundo ", use_color)
        line(f"  {fg}  {bright:<12}  {bg}")
    line()

    line("Apelidos PT-BR: vermelho, verde, azul, amarelo, ciano, rosa, branco, preto")
    line("Estilos PT-BR: negrito, fraco, italico, sublinhado, tachado")
    line("Cores reais: //#ff8800/...  |  fundo real: //bg-#222222/...")
