import builtins
import io

import pytest

import easyansi
from easyansi import activate, deactivate, eprint, is_active


@pytest.fixture(autouse=True)
def reset_builtins():
    """Garante que cada teste comeca e termina com builtins restaurados."""
    deactivate()
    yield
    deactivate()


def test_is_active_false_by_default():
    assert is_active() is False


def test_activate_sets_active():
    activate()
    assert is_active() is True


def test_activate_is_idempotent():
    activate()
    activate()
    assert is_active() is True


def test_deactivate_is_idempotent():
    deactivate()
    assert is_active() is False


def test_activate_makes_print_colorized():
    activate()
    buffer = io.StringIO()
    print("//red/oi/red", file=buffer, color=True)
    assert "\x1b[31moi\x1b[0m" in buffer.getvalue()


def test_deactivate_restores_print():
    activate()
    deactivate()
    buffer = io.StringIO()
    builtins.print("//red/oi/red", file=buffer)
    assert "\x1b" not in buffer.getvalue()
    assert buffer.getvalue() == "//red/oi/red\n"


def test_eprint_works_while_active():
    activate()
    buffer = io.StringIO()
    eprint("//green/ok/green", file=buffer, color=True)
    assert "\x1b[32mok\x1b[0m" in buffer.getvalue()


def test_no_recursion_when_active():
    activate()
    buffer = io.StringIO()
    for _ in range(50):
        print("x", file=buffer, color=False, end="")
    assert buffer.getvalue() == "x" * 50
