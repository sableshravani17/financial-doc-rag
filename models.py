from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime


# ✅ User Table
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)



class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)   
    title = Column(String)
    company_name = Column(String)
    document_type = Column(String)   
    file_path = Column(String)       
    uploaded_by = Column(Integer)   
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class UserRole(Base):
    __tablename__ = "user_roles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    role_id = Column(Integer)