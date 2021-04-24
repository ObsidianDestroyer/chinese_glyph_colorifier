import unicodedata

from typing import Final, List

from glypher.helpers.typing import Bool, String, Bytes
from glypher.utils.encoder import encode


class RadicalBase(object):
    """A base class for inheritance."""
    color: String = 'grey'
    category: Final[String] = 'Lo'
    name: String

    block_start: String
    block_end: String

    radical: String
    alt_radical: String = None
    signature: Bytes
    alt_signature: Bytes


class Human(RadicalBase):
    """Human radical exposed as "亻, a" """
    name = 'human'
    color = '#ffc972'

    block_start = 'U4EBA'
    block_end = 'U513E'

    radical = '人'
    alt_radical = '亻'
    signature = encode(radical)
    alt_signature = encode(alt_radical)


class Heart(RadicalBase):
    """Heart radical exposed as "忄, 心" """
    name = 'heart'
    color = '#ff261e'

    block_start = 'U5FC3'
    block_end = 'U6207'

    radical = '忄'
    alt_radical = '心'
    signature = encode(radical)
    alt_signature = encode(alt_radical)


class Sun(RadicalBase):
    name = 'sun'
    color = '#ec4e10'

    block_start = 'U65E5'
    block_end = 'U66EF'

    radical = '日'
    alt_radical = None
    signature = encode(radical)
    alt_signature = None


class Fire(RadicalBase):
    """Fire radical exposed as "火, 灬" """
    name = 'fire'
    color = '#ff00ff'

    block_start = 'U706B'
    block_end = 'U7229'

    radical = '火'
    alt_radical = '灬'
    signature = encode(radical)
    alt_signature = encode(alt_radical)


class Tree(RadicalBase):
    name = 'tree'
    color = '#009376'

    radical = '木'

    block_start = 'U6728'
    block_end = 'U6B1F'

    signature = encode(radical)


class Water(RadicalBase):
    name = 'water'
    color = '#000000'

    radical = '水'
    alt_radical = '氵'

    block_start = 'U6C34'
    block_end = 'U706A'

    signature = encode(radical)
    alt_signature = encode(alt_radical)


class Metal(RadicalBase):
    name = 'metal'
    color = '#cfcfcf'

    radical = '金'
    alt_radical = '钅'

    block_start = 'U91D1'
    block_end = 'U9484'

    signature = encode(radical)
    alt_signature = encode(alt_radical)


class Earth(RadicalBase):
    name = 'earth'
    color = '#ffff00'

    radical = '土'

    block_start = 'U571F'
    block_end = 'U5901'

    signature = encode(radical)


class Mouth(RadicalBase):
    name = 'mouth'
    color = '#ed5f5f'

    radical = '口'

    block_start = 'U53E3'
    block_end = 'U571'

    signature = encode(radical)


class Woman(RadicalBase):
    name = 'woman'
    color = '#f55bd3'

    radical = '女'

    block_start = 'U5973'
    block_end = 'U5B4F'

    signature = encode(radical)


class Jasper(RadicalBase):
    name = 'jasper'
    color = '#30d5a9'

    radical = '玉'

    block_start = 'U7389'
    block_end = 'U74DB'

    signature = encode(radical)


class Grass(RadicalBase):
    name = 'grass'
    color = '#39ad60'

    radical = '艹'
    alt_radical = '艸'

    block_start = 'U8278'
    block_end = 'U864C'

    signature = encode(radical)
    alt_signature = encode(alt_radical)


class FastWalk(RadicalBase):
    name = 'walk'
    color = '#404040'

    radical = '辶'

    block_start = 'U8FB5'
    block_end = 'U9090'

    signature = encode(radical)
    # alt_signature = encode(alt_radical)


class Food(RadicalBase):
    name = 'food'
    color = '#ebbb4d'

    radical = '食'

    block_start = 'U98DF'
    block_end = 'U9962'

    signature = encode(radical)


__all__ = ['glyphs', 'RadicalBase']

glyphs: List[RadicalBase] = [
    Tree(), Food(), Human(),
    Earth(), Metal(), Water(),
    Grass(), Woman(), Mouth(),
    Jasper(), FastWalk(), Fire(),
    Heart(), Sun(),

]
