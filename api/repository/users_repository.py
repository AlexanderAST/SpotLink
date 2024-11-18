from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.users_model import UsersModel
from api.dto.users_dto import UsersCreateDTO
from sqlalchemy import select

class UsersRepository:
    async def create_user(self, db: AsyncSession, user_data: UsersCreateDTO):
        new_user = UsersModel(
            city = user_data.city,
            username = user_data.username,
            email = user_data.email,
            password = user_data.password
        )
        
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
    
    async def get_user_by_email(self, db:AsyncSession, email:str):
        query = select(UsersModel).where(UsersModel.email == email)
        result = await db.execute(query)
        
        return result.scalars().one()
    
    async def get_user_by_id(self, db:AsyncSession, id:int):
        query = select(UsersModel).where(UsersModel.id == id)
        result = await db.execute(query)
        
        return result.scalars().one()