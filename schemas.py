from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str



class DocumentCreate(BaseModel):
    title: str
    company_name: str
    document_type: str



class RoleCreate(BaseModel):
    name: str



class AssignRole(BaseModel):
    user_id: int
    role_id: int