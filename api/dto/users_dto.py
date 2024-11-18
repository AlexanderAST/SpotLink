from pydantic import BaseModel, EmailStr

class UsersCreateDTO(BaseModel):
    city:str
    username: str
    email: EmailStr
    password: str
    

class UsersCreateResponseDTO(BaseModel):
    id: int
    username: str
    status: str


class UsersAuth(BaseModel):
    email:EmailStr
    password:str