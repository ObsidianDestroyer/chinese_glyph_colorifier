from typing import Dict, List, Union

from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from glypher.structures.radicals import glyphs, RadicalBase
from glypher.data.models.api_models import GlyphResponse
from glypher.helpers.typing import String, Bool, Integer
from glypher.structures.glyphs import Glyph
from glypher.utils.encoder import encode_to_str


router = APIRouter(prefix='/api')
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


@router.post('/colorify')
async def colorize_characters(request: Request) -> JSONResponse:
    form = await request.form()
    text = form.get('text')
    glyphs_list: List[Glyph] = []

    for char in text:
        if radical := decode(char):
            glyphs_list.append(
                Glyph(
                    character=char,
                    radical=[
                        radical.radical,
                        radical.alt_radical,
                    ],
                    color=radical.color,
                    radical_name=radical.name,
                ),
            )
        else:
            glyphs_list.append(
                Glyph(
                    character=char,
                    radical=[],
                ),
            )
    radicals_stat: Dict[String, Integer] = {}
    for glyph in glyphs_list:
        if glyph.radical:
            if glyph.radical[0] not in radicals_stat.keys():
                radicals_stat.update({
                    glyph.radical[0]: 1
                })
            else:
                radicals_stat.update({
                    glyph.radical[0]: radicals_stat[glyph.radical[0]] + 1
                })
    response = GlyphResponse(
        stats=radicals_stat,
        body=[glyph.dict() for glyph in glyphs_list],
    )
    return JSONResponse(response.dict())
