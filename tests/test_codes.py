from easyansi import codes


def test_resolve_single_style():
    assert codes.resolve("bold") == ["1"]
    assert codes.resolve("negrito") == ["1"]


def test_resolve_single_color():
    assert codes.resolve("red") == ["31"]
    assert codes.resolve("vermelho") == ["31"]


def test_resolve_combo_style_and_color():
    assert codes.resolve("bold-blue") == ["1", "34"]


def test_resolve_bright():
    assert codes.resolve("bright-red") == ["91"]
    assert codes.resolve("claro-vermelho") == ["91"]


def test_resolve_background():
    assert codes.resolve("bg-blue") == ["44"]
    assert codes.resolve("fundo-azul") == ["44"]


def test_resolve_bright_background():
    assert codes.resolve("bg-bright-red") == ["101"]


def test_resolve_hex_foreground():
    assert codes.resolve("#ff8800") == ["38;2;255;136;0"]


def test_resolve_hex_background():
    assert codes.resolve("bg-#ff8800") == ["48;2;255;136;0"]


def test_resolve_short_hex():
    assert codes.resolve("#fff") == ["38;2;255;255;255"]


def test_resolve_unknown_returns_none():
    assert codes.resolve("azu") is None
    assert codes.resolve("") is None
    assert codes.resolve("#zzlmno") is None


def test_sequence_format():
    assert codes.sequence(["1", "34"]) == "\x1b[1;34m"
