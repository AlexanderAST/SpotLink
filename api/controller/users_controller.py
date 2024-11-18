from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.service.users_service import oauth2_scheme, UsersService
from api.dto.users_dto import UsersCreateDTO, UsersCreateResponseDTO, UsersAuth
from api.database import get_db
from api.repository.users_repository import UsersRepository

router = APIRouter()
user_service = UsersService(UsersRepository())

@router.post("/sign-up", response_model=UsersCreateResponseDTO)
async def sign_up(user:UsersCreateDTO, db:AsyncSession = Depends(get_db)):
    try:
        created_user = await user_service.create_user(db, user)
        return UsersCreateResponseDTO(
            id = created_user.id,
            username= created_user.username,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/sign-in")
async def sign_in(user:UsersAuth, db:AsyncSession = Depends(get_db)):
    try:
        token = await user_service.auth_user(db, user)
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/validate-token")
async def validate_token(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)):
    
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing or invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        user = await user_service.validate_token(db,token)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))