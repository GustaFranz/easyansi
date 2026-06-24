import io

from easyansi import terminal


class FakeTTY(io.StringIO):
    def isatty(self):
        return True


def test_no_color_env_disables(monkeypatch):
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    monkeypatch.setenv("NO_COLOR", "1")
    assert terminal.supports_color(FakeTTY()) is False


def test_force_color_env_enables(monkeypatch):
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert terminal.supports_color(io.StringIO()) is True


def test_non_tty_is_false(monkeypatch):
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.delenv("TERM", raising=False)
    assert terminal.supports_color(io.StringIO()) is False


def test_tty_is_true(monkeypatch):
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.delenv("TERM", raising=False)
    assert terminal.supports_color(FakeTTY()) is True


def test_term_dumb_is_false(monkeypatch):
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setenv("TERM", "dumb")
    assert terminal.supports_color(FakeTTY()) is False


def test_enable_windows_ansi_is_safe():
    # Nao deve lancar excecao em nenhum SO.
    assert terminal.enable_windows_ansi() in (True, False)
