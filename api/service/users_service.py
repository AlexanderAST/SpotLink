from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.repository.users_repository import UsersRepository
from api.dto.users_dto import UsersCreateDTO, UsersAuth
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from api.config import env

SECRET_KEY = env.str("SECRET_KEY")
ALGORITHM = env.str("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(expires_delta: timedelta, data: dict) -> str:
    to_encode = data.copy()
    now = datetime.utcnow()
    expire = now + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({
        "exp": int(expire.timestamp()),
        "iat": int(now.timestamp()),   
    })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class UsersService:
    def __init__(self, users_repository:UsersRepository):
        self.users_repository = users_repository
    
    async def create_user(self, db:AsyncSession, user_data:UsersCreateDTO):
        
        new_user = UsersCreateDTO(
            city=user_data.city,
            username=user_data.username,
            email= user_data.email,
            password = get_password_hash(user_data.password)
        )
        
        return await self.users_repository.create_user(db, new_user)

    
    async def auth_user(self, db:AsyncSession, login_data: UsersAuth):
        user = await self.users_repository.get_user_by_email(db, login_data.email)
        
        if not user or not verify_password(login_data.password, user.password):
            return {"error":"incorrect email or password"}
        
        access_token = create_access_token(
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
            data={"iat": datetime.utcnow().isoformat(),"user_id": int(user.id),}
        )
        
        return access_token
    
    async def validate_token(self, db:AsyncSession, token:str):
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id : int = payload.get("user_id")
        
        if id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token: missing id",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        user = await self.users_repository.get_user_by_id(db, id)
        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return {"id":user.id, "email": user.email, "username":user.username,"city":user.city}