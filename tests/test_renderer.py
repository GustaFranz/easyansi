from easyansi.parser import parse
from easyansi.renderer import render

RESET = "\x1b[0m"


def r(text, color=True):
    return render(parse(text), color=color)


def test_basic_ansi_output():
    assert r("//red/oi/red") == f"\x1b[31moi{RESET}"


def test_combo_output():
    assert r("//bold-blue/x/bold-blue") == f"\x1b[1;34mx{RESET}"


def test_color_false_is_clean():
    assert r("//bold-blue/x/bold-blue", color=False) == "x"


def test_reset_at_close():
    out = r("a //red/b/red c")
    assert out == f"a \x1b[31mb{RESET} c"


def test_nested_reapplies_outer():
    # Apos fechar o bold, o texto deve continuar vermelho (reaplicado).
    out = r("//red/a //bold/b/bold c/red")
    assert out == f"\x1b[31ma \x1b[1mb{RESET}\x1b[31m c{RESET}"


def test_autoclose_adds_reset():
    out = r("//red/sem fechar")
    assert out.endswith(RESET)


def test_plain_text_unchanged():
    assert r("nada aqui") == "nada aqui"
