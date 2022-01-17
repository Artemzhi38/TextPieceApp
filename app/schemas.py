from enum import Enum

from pydantic import BaseModel, Field


class TextType(str, Enum):
    title = "title"
    paragraph = "paragraph"


class TextPiece(BaseModel):
    text: str = Field(
        ..., title="A piece of pext to store."
    )
    text_type: TextType = Field(
        ..., title="Type of text. Can be 'title' or 'paragraph'."
    )
    document_name: str = Field(
        ...,
        title="Name of the document containing this TextPiece.",
        max_length=50
    )
    page_number: int = Field(
        ..., title="Number of page in the document.", gt=0
    )
