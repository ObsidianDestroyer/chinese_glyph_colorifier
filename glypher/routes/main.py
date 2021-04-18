from typing import Dict, List

from fastapi import status
from fastapi.params import Form
from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import HTTPException

from glypher.structures.radicals import (
    RadicalBase, Human, Heart, Sun, Fire,
)
from glypher.helpers.typing import String
from glypher.structures.glyphs import Glyph
from glypher.helpers.exceptions import (
    CharacterError, WrongCharacterUnicodeBlock,
)

router = APIRouter(prefix='/api')

LAST_COLORIZATION: List[Dict] = []

character_keys: List[RadicalBase] = [
    Human(), Heart(), Sun(), Fire(),
]


@router.get('/colorify')
async def get_last_colorization(request: Request) -> JSONResponse:
    return JSONResponse(LAST_COLORIZATION)


@router.post('/colorify')
async def colorize_characters(text: String = Form(...)) -> JSONResponse:
    global LAST_COLORIZATION
    response: List[Dict] = []
    for char in text:  # type: String
        for radical in character_keys:
            try:
                if radical.inspect_radical(char):
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
            except CharacterError:
                raise HTTPException(
                    detail=str(CharacterError(char)),
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
            except WrongCharacterUnicodeBlock:
                raise HTTPException(
                    detail=str(WrongCharacterUnicodeBlock(char)),
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
    LAST_COLORIZATION = response
    return JSONResponse(response)
