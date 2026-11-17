# Text Extensions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ysskrishna/text-extensions/blob/main/LICENSE)
[![Tests](https://github.com/ysskrishna/text-extensions/actions/workflows/test.yml/badge.svg)](https://github.com/ysskrishna/text-extensions/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/text-extensions)](https://pypi.org/project/text-extensions/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/text-extensions?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/text-extensions)
[![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)
[![Context7](https://img.shields.io/badge/Context7-docs-18181B)](https://context7.com/ysskrishna/text-extensions)
[![Ask DeepWiki](https://img.shields.io/badge/DeepWiki-ask-18181B)](https://deepwiki.com/ysskrishna/text-extensions)

Check if a file or extension is text, and iterate over 300+ known text file types including source code, markup, data formats, and configuration files. Python port of [text-extensions](https://github.com/sindresorhus/text-extensions) npm package.

## Features

- Immutable collection of hundreds of known text file extensions  
- Fast membership checks using `frozenset`  
- Case-insensitive and dot-aware checks  
- Works for both extensions and full file paths  
- Supports dotfiles (e.g., `.gitignore`)  
- Zero dependencies, minimal overhead  

## Installation

```bash
pip install text-extensions
```

Or using `uv`:

```bash
uv add text-extensions
```

## Usage

### Check if an extension is text

```python
from text_extensions import is_text_extension

is_text_extension("txt")      # True
is_text_extension(".py")      # True (dot-aware)
is_text_extension("JS")       # True (case-insensitive)
is_text_extension("png")      # False
```

### Check if a file path has a text extension

```python
from text_extensions import is_text_path

is_text_path("document.txt")              # True
is_text_path("/path/to/file.PY")          # True (case-insensitive)
is_text_path("script.js")                 # True
is_text_path("image.png")                 # False
is_text_path(".gitignore")                # True (dotfile support)
```

### Access the list of text extensions

```python
from text_extensions import TEXT_EXTENSIONS, TEXT_EXTENSIONS_LOWER

# TEXT_EXTENSIONS is a frozenset of all known text extensions
print(len(TEXT_EXTENSIONS))  # Number of supported extensions
"txt" in TEXT_EXTENSIONS     # True
"png" in TEXT_EXTENSIONS     # False

# TEXT_EXTENSIONS_LOWER contains all extensions in lowercase
# Useful for case-insensitive lookups without calling .lower() repeatedly
"TXT" in TEXT_EXTENSIONS_LOWER  # True (case-insensitive)
```

## API Reference

Install with `pip install text-extensions` and import from `text_extensions`. Signatures and descriptions below match the source code of `text_extensions`.

### `TEXT_EXTENSIONS`

Constant: `frozenset` with 329 entries.

### `TEXT_EXTENSIONS_LOWER`

Constant: `frozenset` with 329 entries.

### `is_text_extension(ext: str) -> bool`

Return True if the given file extension is known to be text.

**Example**

```python
from text_extensions import is_text_extension

is_text_extension("txt")  # True
is_text_extension(".png")  # False
```

### `is_text_path(file_path: str) -> bool`

Return True if the file path has a text file extension.

**Example**

```python
from text_extensions import is_text_path

is_text_path("document.txt")  # True
is_text_path("image.png")  # False
is_text_path("/path/to/file.PY")  # True
is_text_path(".gitignore")  # True
```

## Supported Extensions

The package includes support for hundreds of text file extensions, including:

- **Source Code**: py, js, ts, java, c, cpp, go, rs, rb, php, and more
- **Markup**: html, xml, md, markdown, json, yaml, yml, and more
- **Stylesheets**: css, scss, sass, less, styl, and more
- **Configuration**: ini, conf, cfg, json, yaml, and more
- **Data Formats**: csv, tsv, json, xml, sql, and more
- **Documentation**: txt, md, rst, tex, and more
- **Scripts**: sh, bash, zsh, fish, bat, cmd, and more
- And many more...

## Credits

This package is a Python port of the [text-extensions](https://github.com/sindresorhus/text-extensions) npm package by [Sindre Sorhus](https://github.com/sindresorhus).


## Contributing

Contributions are welcome! Please read our [Contributing Guide](https://github.com/ysskrishna/text-extensions/blob/main/CONTRIBUTING.md) for details on our code of conduct, development setup, and the process for submitting pull requests.

## Built and maintained by

Text Extensions is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Changelog

See [CHANGELOG](CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/text-extensions/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://pypi.org/project/text-extensions/">Package on PyPI</a> •
  <a href="https://github.com/ysskrishna/text-extensions/issues">Report Issues</a>
</p>
