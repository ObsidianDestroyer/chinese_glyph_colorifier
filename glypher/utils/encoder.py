from glypher.helpers.typing import Bytes, String


def encode(char: String) -> Bytes:
    return char.encode('unicode_escape')[1:]


def encode_to_str(char: String) -> String:
    return char.encode('unicode_escape')[1:].decode().upper()
