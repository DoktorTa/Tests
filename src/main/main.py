import os
import asyncio

from dotenv import load_dotenv

from src.main.db.base import create_models
from src.main.stock.db import models

print('Start')
dotenv_path = os.path.join(os.path.dirname(__file__), 'dev.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

print('DB start connections')
asyncio.run(create_models())
print('End')