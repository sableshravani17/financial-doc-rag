from fastapi import FastAPI
from database import Base, engine

from routes import user, role, document, rag

app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(user.router, prefix="/auth", tags=["Auth"])
app.include_router(role.router, prefix="/roles", tags=["Roles"])
app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(rag.router, prefix="/rag", tags=["RAG"])