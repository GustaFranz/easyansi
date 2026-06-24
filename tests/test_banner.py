from easyansi.banner import titulo

RESET = "\x1b[0m"


def test_titulo_basic_layout():
    out = titulo("CADASTRO DE ALUNOS", "=", largura=40, color=False)
    lines = out.split("\n")
    assert len(lines) == 3
    assert lines[0] == "=" * 40
    assert lines[1] == "CADASTRO DE ALUNOS".center(40)
    assert lines[2] == "=" * 40


def test_titulo_different_chars():
    assert titulo("X", "-", largura=10, color=False).split("\n")[0] == "-" * 10
    assert titulo("X", "~", largura=10, color=False).split("\n")[0] == "~" * 10


def test_titulo_left_align():
    out = titulo("Titulo", "=", largura=20, alinhar="esquerda", color=False)
    assert out.split("\n")[1] == "Titulo"


def test_titulo_truncates_long_text():
    out = titulo("TEXTO MUITO LONGO AQUI", "=", largura=10, color=False)
    assert out.split("\n")[1] == "TEXTO M..."


def test_titulo_line_style():
    out = titulo("X", "=", largura=5, estilo_linha="blue", color=True)
    line = out.split("\n")[0]
    assert line.startswith("\x1b[34m")
    assert line.endswith(RESET)


def test_titulo_text_style():
    out = titulo("X", "=", largura=5, estilo_texto="bold", color=True)
    title = out.split("\n")[1]
    assert title.startswith("\x1b[1m")
    assert title.endswith(RESET)


def test_titulo_shared_style():
    out = titulo("X", "=", largura=5, estilo="red", color=True)
    lines = out.split("\n")
    assert lines[0].startswith("\x1b[31m")
    assert lines[1].startswith("\x1b[31m")


def test_titulo_inline_tags():
    out = titulo("//red/X/red", "=", largura=5, color=False)
    assert out.split("\n")[1] == "X".center(5)


def test_titulo_invalid_style_failsafe():
    out = titulo("X", "=", largura=5, estilo="invalid-style", color=True)
    assert out.split("\n")[1] == "X".center(5)
