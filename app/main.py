from fastapi import FastAPI
from app.controllers.controller import api
from core.extensions import db  
from app.models.model import *


app = FastAPI()

db.init_app(app)
app.include_router(api)


@app.on_event("startup")
async def app_start():
    print("App start")


@app.on_event("shutdown")
async def app_down():
    print("App down")


