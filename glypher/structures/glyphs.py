from typing import List, Optional

from pydantic import BaseModel

from glypher.helpers.typing import String


class Glyph(BaseModel):
    color: String
    character: String
    radical: List[Optional[String]]
    radical_name: String
