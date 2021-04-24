from typing import Dict, List

from pydantic import BaseModel

from glypher.helpers.typing import String


class FormData(BaseModel):
    text: String


class GlyphResponse(BaseModel):
    stats: Dict
    body: List[Dict]
