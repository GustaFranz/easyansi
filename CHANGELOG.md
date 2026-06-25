# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/).

## [0.5.1] - 2026-06-24

### Added

- Short alias `t()` for `title()` — simpler decorative titles

### Changed

- Docs now recommend `print(title("Text", "="))` as the primary title pattern

## [0.5.0] - 2026-06-24

### Changed

- PyPI distribution name set to `py-easyansi` (import remains `easyansi`)
- Renamed public API identifiers to English: `titulo` → `title`, `perguntar` → `ask`
- Renamed parameters to English: `escopo` → `scope`, `largura` → `width`, `alinhar` → `align`, etc.
- Updated documentation in EN, PT, ES, and ZH to match the new API

## [0.4.0] - 2026-06-24

### Added

- Whole-text styling via `ansi()`, `paint()`, and `.easyansi()`
- Decorative titles with `title()` and `.title()`
- Input scopes for colored prompts and answers (`scope`: `prompt`, `answer`, `both`)
- `ask()` helper for styled input

## [0.2.0] - 2026-06-24

### Added

- Initial release: `//color/` markup syntax, `eprint`, `fmt`, shortcuts, logging helpers
- Windows ANSI auto-activation, fail-safe unknown tags, zero dependencies

[0.5.0]: https://github.com/GustaFranz/easyansi/releases/tag/v0.5.0
[0.4.0]: https://github.com/GustaFranz/easyansi/releases/tag/v0.4.0
[0.2.0]: https://github.com/GustaFranz/easyansi/releases/tag/v0.2.0
