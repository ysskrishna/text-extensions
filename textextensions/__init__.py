import os.path
from textextensions._data import TEXT_EXTENSIONS

__all__ = ["TEXT_EXTENSIONS", "is_text_extension", "is_text_path"]

def is_text_extension(ext: str) -> bool:
    """
    Return True if the given file extension is known to be text.

    Examples:
        >>> is_text_extension("txt")
        True
        >>> is_text_extension(".png")
        False
    """
    return ext.lower().lstrip(".") in TEXT_EXTENSIONS

def is_text_path(file_path: str) -> bool:
    """
    Return True if the file path has a text file extension.

    Examples:
        >>> is_text_path("document.txt")
        True
        >>> is_text_path("image.png")
        False
        >>> is_text_path("/path/to/file.PY")
        True
    """
    _, ext = os.path.splitext(file_path)
    return ext.lstrip(".").lower() in TEXT_EXTENSIONS

