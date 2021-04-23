import unicodedata

from typing import Final, List

from glypher.helpers.typing import Bool, String, Bytes
from glypher.helpers.exceptions import CharacterError, WrongCharacterUnicodeBlock
from glypher.utils.encoder import encode


class RadicalBase(object):
    """A base class for inheritance."""
    color: String = 'grey'
    category: Final[String] = 'Lo'
    name: String

    block_start: String
    block_end: String

    radical: String
    alt_radical: String
    signature: Bytes
    alt_signature: Bytes

    def _decode_unicode_end_block_literal(self) -> String:
        character: String = chr(int(self.block_end.strip('U').zfill(8), 16))
        if unicodedata.category(character) == self.category:
            return character
        raise WrongCharacterUnicodeBlock(character)

    def inspect_radical(self, character: String) -> Bool:
        if unicodedata.category(character) == self.category:
            end_block_character = self._decode_unicode_end_block_literal()
            conditions: List[Bool] = [
                self.radical <= character,
                character <= end_block_character,
            ]
            return all(conditions)
        raise CharacterError(character)


class Human(RadicalBase):
    """Human radical exposed as "亻, a" """
    name = 'human'
    color = 'blue'

    block_start = 'U4EBA'
    block_end = 'U513E'

    radical = '人'
    alt_radical = '亻'
    signature = encode(radical)
    alt_signature = encode(radical)


class Heart(RadicalBase):
    """Heart radical exposed as "忄, 心" """
    name = 'heart'
    color = 'red'

    block_start = 'U5FC3'
    block_end = 'U6207'

    radical = '忄'
    alt_radical = '心'
    signature = encode(radical)
    alt_signature = encode(radical)


class Sun(RadicalBase):
    name = 'sun'
    color = 'green'

    block_start = 'U65E5'
    block_end = 'U66EF'

    radical = '日'
    alt_radical = None
    signature = encode(radical)
    alt_signature = encode(radical)


class Fire(RadicalBase):
    """Fire radical exposed as "火, 灬" """
    name = 'fire'
    color = 'magenta'

    block_start = 'U706B'
    block_end = 'U7229'

    radical = '火'
    alt_radical = '灬'
    signature = encode(radical)
    alt_signature = encode(radical)
