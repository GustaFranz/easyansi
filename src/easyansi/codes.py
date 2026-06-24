"""Tabela de codigos ANSI da EasyAnsi (dados puros, sem logica de I/O).

Este modulo concentra todo o "banco de dados" de estilos e cores. Para
adicionar um novo estilo ou apelido, basta editar os dicionarios abaixo;
nenhum outro modulo precisa mudar.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

ESC = "\x1b"
RESET = "0"
RESET_SEQ = f"{ESC}[0m"

STYLES = {
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "strike": "9",
    "negrito": "1",
    "fraco": "2",
    "italico": "3",
    "sublinhado": "4",
    "tachado": "9",
}

# Cores base (codigo de texto/foreground). Fundo = base + 10. Brilhante = base + 60.
COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "preto": 30,
    "vermelho": 31,
    "verde": 32,
    "amarelo": 33,
    "azul": 34,
    "magenta_pt": 35,
    "rosa": 35,
    "ciano": 36,
    "branco": 37,
}

BG_PREFIX = {"bg", "fundo"}
BRIGHT_PREFIX = {"bright", "claro"}


def _hex_to_rgb(value: str) -> Optional[Tuple[int, int, int]]:
    """Converte '#rgb' ou '#rrggbb' em (r, g, b); retorna None se invalido."""
    h = value[1:]
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    except ValueError:
        return None


def _color_code(token: str, is_bg: bool, is_bright: bool) -> Optional[str]:
    """Resolve um token de cor (nome ou hex) em codigo ANSI; None se invalido."""
    if token.startswith("#"):
        rgb = _hex_to_rgb(token)
        if rgb is None:
            return None
        prefix = "48" if is_bg else "38"
        return f"{prefix};2;{rgb[0]};{rgb[1]};{rgb[2]}"
    base = COLORS.get(token)
    if base is None:
        return None
    if is_bg:
        base += 10
    if is_bright:
        base += 60
    return str(base)


def resolve(name: str) -> Optional[List[str]]:
    """Traduz um nome de tag em uma lista de codigos ANSI.

    Aceita combinacoes separadas por '-', por exemplo:
    'bold', 'blue', 'bold-blue', 'bright-red', 'bold-bright-red',
    'bg-blue', 'bg-bright-red', '#ff8800', 'bg-#ff8800'.

    Retorna a lista de codigos (ex.: ['1', '34']) ou None se qualquer
    parte for desconhecida (o chamador trata isso como texto literal).
    """
    if not name:
        return None
    parts = name.lower().split("-")
    codes: List[str] = []
    i = 0
    total = len(parts)
    while i < total:
        part = parts[i]
        if part in STYLES:
            codes.append(STYLES[part])
            i += 1
            continue

        is_bg = False
        is_bright = False
        if part in BG_PREFIX:
            is_bg = True
            i += 1
            if i >= total:
                return None
            part = parts[i]
        if part in BRIGHT_PREFIX:
            is_bright = True
            i += 1
            if i >= total:
                return None
            part = parts[i]

        code = _color_code(part, is_bg, is_bright)
        if code is None:
            return None
        codes.append(code)
        i += 1

    return codes or None


def sequence(codes: List[str]) -> str:
    """Monta a sequencia ANSI completa a partir de uma lista de codigos."""
    return f"{ESC}[{';'.join(codes)}m"
