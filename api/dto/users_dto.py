from pydantic import BaseModel

class Users(BaseModel):
    City:str
    UserName: str
    Email: str
    Password: str