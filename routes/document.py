from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import shutil
import os

router = APIRouter()   

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/upload")
def upload_document(
    title: str = Form(...),
    company_name: str = Form(...),
    document_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_doc = models.Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        file_path=file_path,
        uploaded_by=1
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    return new_doc


@router.get("/")
def get_documents(db: Session = Depends(get_db)):
    return db.query(models.Document).all()



@router.get("/{doc_id}")
def get_doc(doc_id: int, db: Session = Depends(get_db)):
    return db.query(models.Document).filter(models.Document.id == doc_id).first()


@router.delete("/{doc_id}")
def delete_doc(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Document).filter(models.Document.id == doc_id).first()
    db.delete(doc)
    db.commit()
    return {"message": "Deleted"}



@router.get("/search")
def search(company_name: str, db: Session = Depends(get_db)):
    return db.query(models.Document).filter(
        models.Document.company_name == company_name
    ).all()