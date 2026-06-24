<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/lang-English-blue?style=for-the-badge" alt="English"></a>
  <a href="docs/README.pt.md"><img src="https://img.shields.io/badge/lang-Português-green?style=for-the-badge" alt="Português"></a>
  <a href="docs/README.es.md"><img src="https://img.shields.io/badge/lang-Español-orange?style=for-the-badge" alt="Español"></a>
  <a href="docs/README.zh.md"><img src="https://img.shields.io/badge/lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

<h1 align="center">EasyAnsi</h1>

<p align="center">
  <strong>The easy and practical way to color terminal text.</strong><br>
  Simple commands. No setup. Write color inside your strings like an f-string.<br>
  Zero dependencies · Fail-safe · Built for beginners and daily scripts.
</p>

<p align="center">
  <a href="https://pypi.org/project/easyansi/"><img src="https://img.shields.io/pypi/v/easyansi?label=PyPI&color=blue" alt="PyPI version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/python-%3E%3D3.8-blue" alt="Python >= 3.8">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="Zero dependencies">
  <img src="https://img.shields.io/badge/typing-typed-informational" alt="Typed">
</p>

---

## Overview

**EasyAnsi** is a lightweight Python library that turns plain strings into ANSI-colored terminal output using an intuitive markup syntax inspired by f-strings — not by Rich's bracket syntax.

Write color directly inside your strings:

```python
from easyansi import eprint

quantity = 12
eprint(f"//bold-blue/All {quantity} cookies were sold today/bold-blue")
eprint(f"Only //red/{quantity}/red items left in stock")
```

No configuration. No heavy console object. No crash if a tag is misspelled — unknown names stay as plain text.

---

## Behind the Project

I am **learning Python**. While studying, I noticed that coloring terminal text could be much simpler than what existing libraries offered — and that complexity was getting in the way of my own learning.

I have been an **elementary school teacher for 14 years**. In the classroom, I learned to spot what helps or hinders daily practice: clear instructions, easy-to-remember commands, and tools that do not punish mistakes. That is the lens through which I designed EasyAnsi — not as a programming expert, but as someone who cares about **learning, teaching, and everyday practicality**.

**Transparency:** this library was built with the support of **artificial intelligence**. I prefer to say that openly rather than pretend I master everything in this codebase. I am still building my technical skills in Python — and EasyAnsi is part of that journey.

What I genuinely bring is the experience of someone who teaches every day: noticing unnecessary barriers, simplifying the path, and thinking about those who are just starting out. EasyAnsi comes from that combination — the curiosity of a learner, the sensitivity of a teacher, and honesty about how it was made.

### What 14 years in the classroom taught me about code

| In the classroom | In EasyAnsi |
| --- | --- |
| Mistakes must not block learning | Unknown tags become plain text — the program never crashes |
| Short, clear instructions | `//color/` syntax as easy to remember as an f-string |
| See before you memorize | `preview()` shows every color in your terminal |
| Ready-to-use daily tools | `success()`, `error()`, `setup_logging()` — one command and done |

Using AI does not make me an impostor: I am someone still learning who **spotted a real need** and chose an honest way to address it — with the same care I put into preparing a lesson to make my students' lives easier.

---

## Our Goal: Easier and More Practical

EasyAnsi exists for one reason: **make terminal colors accessible to everyone**, not just experts.

| What you want | EasyAnsi | Typical heavy libraries |
| --- | --- | --- |
| Start in 30 seconds | `from easyansi import eprint` | Configure a Console, learn markup rules |
| Color one word | `//red/{value}/red` inside f-string | Wrap objects, build Text segments |
| Say "success" | `success("Done")` | Build custom renderables |
| Enable logging colors | `setup_logging()` — one line | Custom handlers, themes, plugins |
| Wrong tag name | Stays as plain text (no crash) | May raise markup errors |

**Philosophy:** fewer concepts, fewer imports, commands you can remember and reuse every day.

---

## Practical Commands (Cheat Sheet)

Copy and use — no extra setup required:

```python
from easyansi import eprint, einput, fmt, success, error, warning, info, red, green, bold

# Print with color (most common)
eprint("//green/Hello!/green")
eprint(f"Score: //bold-blue/{score}/bold-blue")

# One-word shortcuts
print(red("error"), green("ok"), bold("title"))
print(bold(red("critical")))                  # chain shortcuts
print("//bg-yellow/warning on yellow/bg-yellow")  # with activate()

# Status lines (ready to go)
success("Saved")
error("Failed")
warning("Slow connection")
info("Port 8080")

# Input with colored prompt
name = einput("//cyan/Name/cyan: ")

# String only (no print)
text = fmt("//yellow/warning/yellow")

# See all colors in terminal
import easyansi; easyansi.preview()
```

**Logging in one line:**

```python
from easyansi.logging import setup_logging
setup_logging()          # done — logging.info() is now colored
```

---

## Features

| Feature | Description |
| --- | --- |
| **Simple syntax** | `//color/text/color` — open with `//name/`, close with `/name` or `//` |
| **Partial coloring** | Color one word inside an f-string without wrapping the whole line |
| **Styles + colors** | Combine with `-`: `bold-blue`, `italic-underline-red` |
| **True colors** | Hex support: `//#ff8800/orange/#ff8800` |
| **Backgrounds** | `bg-blue`, `bg-#222222` |
| **Bilingual names** | English + Portuguese aliases (`negrito`, `vermelho`, …) |
| **Direct shortcuts** | `red()`, `bold()`, `green()` — great for IDE autocomplete |
| **Status helpers** | `success()`, `error()`, `warning()`, `info()` |
| **Colored logging** | Drop-in `ColorFormatter` for Python's `logging` module |
| **Fail-safe parser** | URLs like `https://` and unknown tags never break output |
| **Smart output** | Auto plain text when piped, redirected, or `NO_COLOR` is set |
| **Windows ready** | VT/ANSI enabled automatically on import |
| **Zero deps** | Stdlib only — installs anywhere |

---

## Requirements

- Python **3.8+**
- A terminal that supports ANSI escape codes (enabled automatically on Windows 10+)

---

## Installation

```bash
pip install easyansi
```

From source:

```bash
git clone https://github.com/seu-usuario/easyansi.git
cd easyansi
pip install -e ".[dev]"
```

---

## Quick Start

**Recommended — use normal `print` and `input`:**

```python
import easyansi

easyansi.activate()   # one line at the top of your script

print("//green/Everything OK!/green")
print(f"Stock: //red/{3}/red units remaining")
name = input("Enter //cyan/your name/cyan: ")
```

No need to rename functions. Call `easyansi.deactivate()` to restore the originals.

**Alternative — explicit `eprint` / `einput`:**

```python
from easyansi import eprint, einput, fmt

eprint("//green/Everything OK!/green")
eprint("Stock: //red/3/red units remaining")
name = einput("Enter //cyan/your name/cyan: ")
message = fmt("//yellow/warning/yellow")
```

---

## Syntax Guide

### Opening and closing tags

| Pattern | Meaning | Example |
| --- | --- | --- |
| `//name/` | Open tag | `//red/` |
| `/name` | Close tag (explicit) | `/red` |
| `//` | Close last open tag | `//green/text//` |

### Combine styles and colors

Use `-` to stack attributes (examples assume `easyansi.activate()` was called):

```python
print("//bold-blue/header/bold-blue")
print("//italic-underline-magenta/highlight/italic-underline-magenta")
print("//bg-yellow/black text on yellow/bg-yellow")
print("//#ff8800/exact orange/#ff8800")
```

### Works inside f-strings

```python
value = 42
print(f"Result: //green/{value}/green points")
```

### Escape literal slashes

```python
print(r"path: \/usr\/local/bin")
```

### Fail-safe by design

Only **known** style/color names are interpreted. Everything else stays literal:

```python
print("Visit https://example.com/page")   # URL untouched
print("//typo/text/typo")                 # treated as plain text
```

---

## Customization Examples

Everyday patterns you can copy and adapt (with `activate()`):

```python
import easyansi
easyansi.activate()

# entire line
print("//green/Saved successfully/green")

# only one word
score = 10
print(f"Score: //bold-blue/{score}/bold-blue points")

# style + color combined
print("//italic-underline-magenta/Important note/italic-underline-magenta")

# background and hex
print("//bg-yellow/black on yellow/bg-yellow")
print("//#ff8800/custom orange/#ff8800")

# Portuguese aliases also work
print("//negrito-vermelho/Error/negrito-vermelho")
```

---

## API Reference

### Core functions

| Function | Description |
| --- | --- |
| `activate()` | Makes global `print` and `input` interpret EasyAnsi markup |
| `deactivate()` | Restores original `print` and `input` |
| `is_active()` | Returns whether `activate()` is in effect |
| `fmt(text, *, color=None)` | Returns formatted string (ANSI or plain) |
| `eprint(*values, sep=" ", end="\n", file=None, color=None, flush=False)` | Colored `print` |
| `einput(prompt="", *, color=None)` | Colored `input` |
| `preview(file=None)` | Prints all available styles and colors |

**`color` parameter:** `None` = auto-detect terminal · `True` = force ANSI · `False` = plain text

### Color shortcuts

`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white`

```python
from easyansi import red, green, yellow, blue, magenta, cyan, white, black

print(red("error"), green("success"), yellow("warning"))
print(blue("info"), magenta("highlight"), cyan("prompt"), white("plain"))
print(black("dark text"))
```

### Style shortcuts

`bold` · `dim` · `italic` · `underline` · `strike` · `style(name, text)`

```python
from easyansi import bold, dim, italic, underline, strike, style, red

print(bold("title"), dim("secondary"), italic("note"))
print(underline("link"), strike("removed"))
print(bold(red("critical")))                 # chain shortcuts
print(style("bold-blue", "custom combo"))   # any name via style()
```

All shortcuts accept `color=None|True|False`.

### Status messages

```python
from easyansi import success, error, warning, info

success("Deploy completed")
error("Connection failed")
warning("Cache is stale")
info("Listening on port 8000")
```

Symbols fall back to ASCII (`[OK]`, `[ERRO]`) when the terminal encoding cannot render Unicode.

---

## Colored Logging

Integrates with Python's standard `logging` module. Log levels are colored in the terminal; output stays clean in files and when `NO_COLOR` is set.

```python
import logging
from easyansi.logging import ColorFormatter, setup_logging

# Option 1 — attach to existing setup
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
logging.root.addHandler(handler)
logging.info("Server started")

# Option 2 — one-line setup
setup_logging(level=logging.INFO)
logging.warning("Cache outdated")
logging.error("Connection failed")
```

**Default level colors:**

| Level | Style |
| --- | --- |
| DEBUG | `dim` |
| INFO | `cyan` |
| WARNING | `yellow` |
| ERROR | `red` |
| CRITICAL | `bold-red` |

**EasyAnsi markup in log messages:**

```python
setup_logging(markup=True, force=True)
logging.info("//green/Deploy completed/green")
```

**Custom level colors (optional):**

```python
import logging
from easyansi.logging import ColorFormatter, setup_logging

handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter(level_colors={
    logging.DEBUG: "dim",
    logging.INFO: "green",
    logging.WARNING: "yellow",
    logging.ERROR: "bold-red",
    logging.CRITICAL: "bold-red",
}))
logging.root.addHandler(handler)
```

**`ColorFormatter` parameters:** `fmt`, `datefmt`, `color`, `markup`, `level_colors`, `stream`

---

## Style & Color Reference

### Text styles

| English | Portuguese | Tag | Preview |
| --- | --- | --- | --- |
| Bold | Negrito | `bold` / `negrito` | <b>sample</b> |
| Dim | Fraco | `dim` / `fraco` | <span style="color:#888">sample</span> |
| Italic | Itálico | `italic` / `italico` | <i>sample</i> |
| Underline | Sublinhado | `underline` / `sublinhado` | <u>sample</u> |
| Strikethrough | Tachado | `strike` / `tachado` | <s>sample</s> |

```python
print("//bold/Bold/bold  //dim/Dim/dim  //italic/Italic/italic")
print("//underline/Underline/underline  //strike/Strikethrough/strike")
```

### Named colors

| English | Portuguese | Tag | Preview |
| --- | --- | --- | --- |
| Black | Preto | `black` / `preto` | <span style="background:#1e1e1e;color:#fff;padding:0 6px">████</span> |
| Red | Vermelho | `red` / `vermelho` | <span style="color:#cd3131">████ red</span> |
| Green | Verde | `green` / `verde` | <span style="color:#13a10e">████ green</span> |
| Yellow | Amarelo | `yellow` / `amarelo` | <span style="color:#c19c00">████ yellow</span> |
| Blue | Azul | `blue` / `azul` | <span style="color:#0451a5">████ blue</span> |
| Magenta | Rosa | `magenta` / `rosa` | <span style="color:#bc3fbc">████ magenta</span> |
| Cyan | Ciano | `cyan` / `ciano` | <span style="color:#059fc0">████ cyan</span> |
| White | Branco | `white` / `branco` | <span style="background:#e8e8e8;color:#333;padding:0 6px;border:1px solid #ccc">████</span> |

```python
print("//red/red  //green/green  //yellow/yellow  //blue/blue")
print("//magenta/magenta  //cyan/cyan  //white/white  //black/black")
```

### Variants

| Variant | Tag | Preview |
| --- | --- | --- |
| Bright | `bright-red`, `claro-vermelho` | <span style="color:#ff5555">████ bright</span> |
| Background | `bg-blue`, `fundo-azul` | <span style="background:#0451a5;color:#fff;padding:0 6px"> bg blue </span> |
| True color (hex) | `#ff8800`, `bg-#222222` | <span style="color:#ff8800">████</span> <span style="background:#222;color:#fff;padding:0 6px"> bg </span> |

```python
print("//bright-red/bright/bright-red")
print("//bg-blue/blue background/bg-blue")
print("//bg-#222222/dark panel/bg-#222222")
print("//#ff8800/exact hex color/#ff8800")
```

### Portuguese aliases

English tags and Portuguese aliases are interchangeable:

```python
print("//negrito-vermelho/error/negrito-vermelho")
print("//fundo-amarelo/warning on yellow/fundo-amarelo")
```

### Discover everything in your terminal

```python
import easyansi
easyansi.preview()
```

---

## Smart Output Behavior

EasyAnsi follows community conventions and behaves correctly in all environments:

| Condition | Behavior |
| --- | --- |
| Interactive terminal (TTY) | ANSI colors applied |
| Piped / redirected output | Plain text (no escape codes) |
| `NO_COLOR` env var set | Plain text ([no-color.org](https://no-color.org/)) |
| `FORCE_COLOR` env var set | Colors forced on |
| `TERM=dumb` | Plain text |
| Windows 10+ | VT mode enabled on import |

Manual override:

```python
from easyansi import fmt

fmt("//red/error/red", color=True)   # always colored
fmt("//red/error/red", color=False)  # always plain — good for files/export
```

---

## Architecture

Modular design with minimal coupling — each module has a single responsibility:

```
string → parser.parse → tokens → renderer.render → output
                  ↑                      ↑
              codes.py            terminal.py (TTY / NO_COLOR)
```

| Module | Role |
| --- | --- |
| `codes.py` | ANSI code tables and name resolution |
| `parser.py` | Markup tokenization (stack, nesting, escape) |
| `renderer.py` | Token → ANSI string (or plain text) |
| `terminal.py` | Environment detection, Windows VT |
| `api.py` | `fmt`, `eprint`, `einput` |
| `shortcuts.py` | Direct color/style functions and status helpers |
| `logging.py` | `ColorFormatter`, `setup_logging` |
| `preview.py` | Visual palette discovery |

---

## Development

```bash
pip install -e ".[dev]"
pytest
```

Run tests with the source layout:

```bash
PYTHONPATH=src pytest
```

---

## Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new behavior
4. Ensure `pytest` passes
5. Open a pull request

---

## Roadmap

- [ ] Accessibility themes (high contrast palettes)
- [ ] HTML / PDF export backends
- [ ] Colored tracebacks in logging

---

## License

MIT — see [LICENSE](LICENSE).

---

<p align="center">
  Made with care for developers who want practical terminal color — easy commands, zero overhead.
</p>
