from typing import Dict, List, Union

from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from glypher.structures.radicals import glyphs, RadicalBase

from glypher.helpers.typing import String, Bool
from glypher.structures.glyphs import Glyph
from glypher.utils.encoder import encode_to_str


router = APIRouter(prefix='/api')

LAST_COLORIZATION: List[Dict] = []

mapped = {
    glyph.radical: glyph for glyph in glyphs
}


def decode(character: String) -> Union[RadicalBase, Bool]:
    for glyph in glyphs:
        character_code: String = encode_to_str(character)
        conditions: List[Bool] = [
            glyph.block_start <= character_code,
            glyph.block_end >= character_code,
        ]
        if all(conditions):
            return mapped.get(glyph.radical)


@router.get('/colorify')
async def get_last_colorization(request: Request) -> JSONResponse:
    return JSONResponse(LAST_COLORIZATION)


@router.post('/colorify')
async def colorize_characters(request: Request) -> JSONResponse:
    global LAST_COLORIZATION
    form = await request.form()
    text = form.get('text')

    response: List[Dict] = []
    for char in text:
        if radical := decode(char):
            response.append(
                Glyph(
                    character=char,
                    radical=[
                        radical.radical,
                        radical.alt_radical,
                    ],
                    color=radical.color,
                    radical_name=radical.name,
                ).dict(),
            )
        else:
            response.append(
                Glyph(
                    character=char,
                    radical=[],
                ).dict(),
            )
    LAST_COLORIZATION = response
    from pprint import pprint
    # pprint(response)
    return JSONResponse(response)
