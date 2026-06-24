import io
import logging

import pytest

from easyansi.logging import ColorFormatter, setup_logging

RESET = "\x1b[0m"


def _record(level, msg="mensagem"):
    return logging.LogRecord(
        name="test",
        level=level,
        pathname=__file__,
        lineno=1,
        msg=msg,
        args=(),
        exc_info=None,
    )


def test_formatter_colors_info_level():
    formatter = ColorFormatter(color=True)
    line = formatter.format(_record(logging.INFO))
    assert "\x1b[36mINFO\x1b[0m" in line
    assert "mensagem" in line


def test_formatter_colors_error_level():
    formatter = ColorFormatter(color=True)
    line = formatter.format(_record(logging.ERROR))
    assert "\x1b[31mERROR\x1b[0m" in line


def test_formatter_critical_is_bold_red():
    formatter = ColorFormatter(color=True)
    line = formatter.format(_record(logging.CRITICAL))
    assert "\x1b[1;31mCRITICAL\x1b[0m" in line


def test_formatter_without_color_is_clean():
    formatter = ColorFormatter(color=False)
    line = formatter.format(_record(logging.INFO))
    assert "\x1b" not in line
    assert line == "INFO | mensagem"


def test_formatter_respects_no_color_env(monkeypatch):
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    monkeypatch.setenv("NO_COLOR", "1")
    formatter = ColorFormatter(stream=io.StringIO())
    line = formatter.format(_record(logging.WARNING))
    assert "\x1b" not in line


def test_formatter_markup_interprets_easyansi():
    formatter = ColorFormatter(color=True, markup=True)
    line = formatter.format(_record(logging.INFO, "//green/ok/green"))
    assert f"\x1b[32mok{RESET}" in line


def test_formatter_markup_false_leaves_tags_literal():
    formatter = ColorFormatter(color=True, markup=False)
    line = formatter.format(_record(logging.INFO, "//green/ok/green"))
    assert "//green/ok/green" in line
    assert "\x1b[32mok" not in line


def test_url_in_message_stays_intact_with_markup():
    formatter = ColorFormatter(color=True, markup=True)
    msg = "veja https://exemplo.com/pagina"
    line = formatter.format(_record(logging.INFO, msg))
    assert msg in line


def test_setup_logging_configures_root():
    setup_logging(level=logging.DEBUG, force=True)
    assert logging.root.level == logging.DEBUG
    assert len(logging.root.handlers) >= 1
    assert isinstance(logging.root.handlers[0].formatter, ColorFormatter)


def test_setup_logging_writes_colored_line(monkeypatch):
    buffer = io.StringIO()
    setup_logging(level=logging.INFO, color=True, stream=buffer, force=True)
    logging.info("teste")
    output = buffer.getvalue()
    assert "\x1b[36mINFO\x1b[0m" in output
    assert "teste" in output
