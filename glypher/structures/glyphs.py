from typing import List, Optional

from pydantic import BaseModel
from pydantic.fields import Field

from glypher.helpers.typing import String


class Glyph(BaseModel):
    color: Optional[String] = Field('#ebebeb')
    character: Optional[String]
    radical: List[Optional[String]]
    radical_name: Optional[String]
