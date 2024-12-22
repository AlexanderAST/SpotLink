from fastapi import FastAPI, APIRouter
from api.controller import hello_controller, users_controller

app = FastAPI()

app.include_router(hello_controller.router) 
app.include_router(users_controller.router)
