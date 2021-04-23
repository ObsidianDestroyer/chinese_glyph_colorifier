from glypher.helpers.typing import String


class CharacterError(Exception):
    """Custom exception to handle invalid chars passing in program."""

    def __init__(
        self,
        char: String,
        message: String = (
            r'You have passed invalid character "{char!r}", '
            'which not in CJK table!'
        ),
    ) -> None:
        self.char: String = char
        self.message: String = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(char=self.char)


class WrongCharacterUnicodeBlock(Exception):
    def __init__(
        self,
        code: String,
        message: String = (
            r'You have passed invalid Unicode block code "{code!r}", '
            'which not in CJK range!'
        ),
    ) -> None:
        self.code: String = code
        self.message: String = message

    def __str__(self):
        return self.message.format(code=self.code)
