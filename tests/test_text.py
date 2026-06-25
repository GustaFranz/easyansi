import io

import easyansi
from easyansi import ansi, ask, paint, title

RESET = "\x1b[0m"


def test_ansi_easyansi_whole_text():
    out = ansi("Ola").easyansi("bold-blue").render(color=True)
    assert out == f"\x1b[1;34mOla{RESET}"


def test_ansi_render_without_color():
    out = ansi("Ola").easyansi("bold-blue").render(color=False)
    assert out == "Ola"


def test_ansi_title_render():
    out = ansi("CADASTRO").title("=", width=10).render(color=False)
    lines = out.split("\n")
    assert lines[0] == "=" * 10
    assert lines[1] == "CADASTRO".center(10)


def test_ansi_read_prompt_scope(monkeypatch):
    monkeypatch.setattr("easyansi.text._builtin_input", lambda prompt: "Gustavo")
    out = ansi("Nome?").easyansi("bold-blue", scope="prompt").read(color=True)
    assert out == "Gustavo"


def test_ansi_read_answer_scope(monkeypatch):
    captured = {}

    def fake_input(prompt):
        captured["prompt"] = prompt
        return "Gustavo"

    monkeypatch.setattr("easyansi.text._builtin_input", fake_input)
    out = ansi("Nome?").easyansi("green", scope="answer").read(color=True)
    assert captured["prompt"] == "Nome?"
    assert out == f"\x1b[32mGustavo{RESET}"


def test_ansi_read_both_scope(monkeypatch):
    captured = {}

    def fake_input(prompt):
        captured["prompt"] = prompt
        return "Gustavo"

    monkeypatch.setattr("easyansi.text._builtin_input", fake_input)
    out = ansi("Nome?").easyansi("bold-blue", scope="both").read(color=True)
    assert captured["prompt"] == f"\x1b[1;34mNome?{RESET}"
    assert out == f"\x1b[1;34mGustavo{RESET}"


def test_ansi_read_text_scope_colors_prompt(monkeypatch):
    captured = {}

    def fake_input(prompt):
        captured["prompt"] = prompt
        return "Ana"

    monkeypatch.setattr("easyansi.text._builtin_input", fake_input)
    out = ansi("Nome?").easyansi("blue").read(color=True)
    assert captured["prompt"] == f"\x1b[34mNome?{RESET}"
    assert out == "Ana"


def test_eprint_ansi_text(monkeypatch):
    buffer = io.StringIO()
    easyansi.eprint(ansi("Oi").easyansi("red"), file=buffer, color=True)
    assert buffer.getvalue() == f"\x1b[31mOi{RESET}\n"


def test_einput_ansi_text(monkeypatch):
    monkeypatch.setattr("easyansi.text._builtin_input", lambda prompt: "Maria")
    out = easyansi.einput(ansi("Nome?").easyansi("green", scope="answer"), color=True)
    assert out == f"\x1b[32mMaria{RESET}"


def test_ask_functional(monkeypatch):
    monkeypatch.setattr("easyansi.text._builtin_input", lambda prompt: "Joao")
    out = ask("Idade?", prompt_style="bold", answer_style="cyan", color=True)
    assert out == f"\x1b[36mJoao{RESET}"


def test_paint_alias():
    assert paint("x", "red", color=True) == f"\x1b[31mx{RESET}"


def test_title_function():
    out = title("MENU", "-", width=8, color=False)
    assert out.split("\n")[0] == "-" * 8


def test_t_is_title_alias():
    import easyansi

    assert easyansi.t is easyansi.title
    assert easyansi.t("X", "=", width=5, color=False) == title("X", "=", width=5, color=False)


def test_ansi_print_method(monkeypatch):
    buffer = io.StringIO()
    monkeypatch.setattr("sys.stdout", buffer)
    ansi("Ok").easyansi("green").print(color=True)
    assert buffer.getvalue() == f"\x1b[32mOk{RESET}\n"
