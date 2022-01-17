from typing import Optional

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder

from app.elastic_search_funcs import (indexing_of_text_piece,
                                      parametrized_search_of_text_pieces,
                                      show_all_text_pieces)
from app.schemas import TextPiece, TextType

app = FastAPI()
TEXT_PIECE_PATH = '/text_piece/'


@app.get(
    TEXT_PIECE_PATH,
    response_description="Result of search in 'text-pieces' index.",
    status_code=status.HTTP_200_OK
)
def show_text_pieces(
        text: Optional[str] = None,
        text_type: Optional[TextType] = None,
        document_name: Optional[str] = None,
        page_number: Optional[int] = None
):
    params = {
        param: value for param, value
        in zip(("text", "text_type", "document_name", "page_number"),
               (text, text_type, document_name, page_number))
        if value
    }
    if not params:
        return show_all_text_pieces()
    return parametrized_search_of_text_pieces(params)


@app.post(
    TEXT_PIECE_PATH,
    response_description="Text piece has been added to index.",
    status_code=status.HTTP_201_CREATED
)
def index_text_piece(item: TextPiece):
    return indexing_of_text_piece(jsonable_encoder(item))
