from easyansi.parser import Token, parse


def kinds(text):
    return [t.kind for t in parse(text)]


def test_plain_text():
    assert parse("ola mundo") == [Token("text", "ola mundo")]


def test_simple_open_close():
    tokens = parse("//red/oi/red")
    assert tokens[0] == Token("open", "red", ("31",))
    assert tokens[1] == Token("text", "oi")
    assert tokens[2] == Token("close", "red")


def test_partial_coloring():
    tokens = parse("Sobrou //blue/1/blue item")
    assert kinds("Sobrou //blue/1/blue item") == ["text", "open", "text", "close", "text"]
    assert tokens[0].value == "Sobrou "
    assert tokens[-1].value == " item"


def test_generic_close():
    tokens = parse("//green/ok//")
    assert tokens[-1] == Token("close", "")


def test_nested_tags():
    tokens = parse("//red/a //bold/b/bold c/red")
    assert kinds("//red/a //bold/b/bold c/red") == [
        "open",
        "text",
        "open",
        "text",
        "close",
        "text",
        "close",
    ]


def test_unknown_name_is_literal():
    # 'azu' nao resolve, entao o trecho fica literal
    assert parse("//azu/x") == [Token("text", "//azu/x")]


def test_url_is_not_broken():
    text = "veja https://exemplo.com/pagina aqui"
    assert parse(text) == [Token("text", text)]


def test_unclosed_tag_is_autoclosed():
    tokens = parse("//red/sem fechar")
    assert tokens[0].kind == "open"
    assert tokens[-1] == Token("close", "")


def test_escape_slash():
    assert parse(r"a\/b") == [Token("text", "a/b")]


def test_escape_double_slash_not_a_tag():
    tokens = parse(r"\//red/x")
    assert tokens[0].value.startswith("/")
