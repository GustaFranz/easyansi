from easyansi.banner import title

RESET = "\x1b[0m"


def test_title_basic_layout():
    out = title("CADASTRO DE ALUNOS", "=", width=40, color=False)
    lines = out.split("\n")
    assert len(lines) == 3
    assert lines[0] == "=" * 40
    assert lines[1] == "CADASTRO DE ALUNOS".center(40)
    assert lines[2] == "=" * 40


def test_title_different_chars():
    assert title("X", "-", width=10, color=False).split("\n")[0] == "-" * 10
    assert title("X", "~", width=10, color=False).split("\n")[0] == "~" * 10


def test_title_left_align():
    out = title("Titulo", "=", width=20, align="left", color=False)
    assert out.split("\n")[1] == "Titulo"


def test_title_truncates_long_text():
    out = title("TEXTO MUITO LONGO AQUI", "=", width=10, color=False)
    assert out.split("\n")[1] == "TEXTO M..."


def test_title_line_style():
    out = title("X", "=", width=5, line_style="blue", color=True)
    line = out.split("\n")[0]
    assert line.startswith("\x1b[34m")
    assert line.endswith(RESET)


def test_title_text_style():
    out = title("X", "=", width=5, text_style="bold", color=True)
    title_line = out.split("\n")[1]
    assert title_line.startswith("\x1b[1m")
    assert title_line.endswith(RESET)


def test_title_shared_style():
    out = title("X", "=", width=5, style="red", color=True)
    lines = out.split("\n")
    assert lines[0].startswith("\x1b[31m")
    assert lines[1].startswith("\x1b[31m")


def test_title_inline_tags():
    out = title("//red/X/red", "=", width=5, color=False)
    assert out.split("\n")[1] == "X".center(5)


def test_title_invalid_style_failsafe():
    out = title("X", "=", width=5, style="invalid-style", color=True)
    assert out.split("\n")[1] == "X".center(5)
