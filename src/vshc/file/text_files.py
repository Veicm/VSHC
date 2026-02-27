from pathlib import Path

__all__ = ["read_text_file"]


def read_text_file(path: Path | str) -> str:
    """
    Read the full content of a UTF-8 encoded text file and return it as a string.

    The function reads the entire file into memory.
    It assumes UTF-8 encoding and propagates any I/O related exceptions.

    Example:
        File content: "Hello"
        -> returns "Hello"

    Args:
        path (Path | str):
            Absolute or relative path to the text file.

    Returns:
        str:
            The complete file content.
    """
    return Path(path).read_text(encoding="utf-8")
