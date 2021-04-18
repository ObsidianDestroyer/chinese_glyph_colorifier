from pydantic import BaseModel

from glypher.helpers.typing import String


class FormData(BaseModel):
    text: String
