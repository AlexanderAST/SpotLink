from fastapi import FastAPI, APIRouter
from api.controller import hello_controller

app = FastAPI()

app.include_router(hello_controller.router) 