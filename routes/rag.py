from fastapi import APIRouter
from pydantic import BaseModel

from rag.rag_utils import (
    index_document,
    search_documents,
    get_context_by_doc,
    remove_document_by_id
)

router = APIRouter()


class IndexRequest(BaseModel):
    file_path: str
    document_id: int


class QueryRequest(BaseModel):
    query: str


@router.post("/index-document")
def index_doc(request: IndexRequest):
    index_document(request.file_path, request.document_id)
    return {"message": "Document indexed successfully"}



@router.post("/search")
def search(request: QueryRequest):
    results = search_documents(request.query)
    return {"results": results}



@router.get("/context/{document_id}")
def get_context(document_id: int):
    context = get_context_by_doc(document_id)
    return {"context": context}



@router.delete("/remove-document/{document_id}")
def remove_doc(document_id: int):
    remove_document_by_id(document_id)
    return {"message": "Document removed from vector DB"}