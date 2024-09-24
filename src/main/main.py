import os

from dotenv import load_dotenv
from fastapi import FastAPI

from src.main.stock.api.router import router as stock_router

# TODO: Импорт переменных пока не работает. Указать папку
dotenv_path = os.path.join(os.path.dirname(__file__), 'dev.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

KTS = FastAPI()
KTS.include_router(stock_router)
