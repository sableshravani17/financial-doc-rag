from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/create")
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    new_role = models.Role(name=role.name)
    db.add(new_role)
    db.commit()
    return {"message": "Role created"}



@router.post("/assign-role")
def assign_role(data: schemas.AssignRole, db: Session = Depends(get_db)):
    user_role = models.UserRole(
        user_id=data.user_id,
        role_id=data.role_id
    )
    db.add(user_role)
    db.commit()
    return {"message": "Role assigned"}



@router.get("/users/{user_id}/roles")
def get_roles(user_id: int, db: Session = Depends(get_db)):
    roles = db.query(models.UserRole).filter(
        models.UserRole.user_id == user_id
    ).all()
    return roles



@router.get("/users/{user_id}/permissions")
def get_permissions(user_id: int, db: Session = Depends(get_db)):
    user_role = db.query(models.UserRole).filter(
        models.UserRole.user_id == user_id
    ).first()
    
    if not user_role:
        return {"message": "No role assigned"}

    if user_role.role_id == 1:
        return {"role": "Admin", "permissions": "Full access"}
    elif user_role.role_id == 2:
        return {"role": "Analyst", "permissions": "Upload & Edit"}
    elif user_role.role_id == 3:
        return {"role": "Auditor", "permissions": "Review"}
    elif user_role.role_id == 4:
        return {"role": "Client", "permissions": "View only"}
    
    return {"message": "Unknown role"}