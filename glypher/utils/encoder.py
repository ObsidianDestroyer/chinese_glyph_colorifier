from glypher.helpers.typing import Bytes, String


def encode(char: String) -> Bytes:
    return char.encode('unicode_escape')[1:]

