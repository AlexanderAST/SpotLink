from sqlalchemy import Column, Integer, String
from api.database import Base


class UsersModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)