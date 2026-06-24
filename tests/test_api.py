import io

import easyansi
from easyansi import fmt, shortcuts

RESET = "\x1b[0m"


def test_fmt_with_color():
    assert fmt("//red/oi/red", color=True) == f"\x1b[31moi{RESET}"


def test_fmt_without_color():
    assert fmt("//red/oi/red", color=False) == "oi"


def test_eprint_writes_to_file(monkeypatch):
    buffer = io.StringIO()
    easyansi.eprint("//red/oi/red", file=buffer, color=True)
    assert buffer.getvalue() == f"\x1b[31moi{RESET}\n"


def test_eprint_multiple_values_and_sep():
    buffer = io.StringIO()
    easyansi.eprint("a", "b", sep="-", file=buffer, color=False)
    assert buffer.getvalue() == "a-b\n"


def test_eprint_non_string_value():
    buffer = io.StringIO()
    easyansi.eprint(123, file=buffer, color=False)
    assert buffer.getvalue() == "123\n"


def test_shortcut_red_with_color():
    assert shortcuts.red("x", color=True) == f"\x1b[31mx{RESET}"


def test_shortcut_failsafe_without_color():
    assert shortcuts.red("x", color=False) == "x"


def test_shortcut_chaining():
    out = shortcuts.bold(shortcuts.red("x", color=True), color=True)
    assert out == f"\x1b[1m\x1b[31mx{RESET}{RESET}"


def test_status_success(monkeypatch):
    buffer = io.StringIO()
    shortcuts.success("ok", file=buffer)
    assert "ok" in buffer.getvalue()
