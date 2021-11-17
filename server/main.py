import uvicorn
import os
import sys

from fastapi import FastAPI

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from server.common.create_app import app_generator
from server.common.const import get_settings

os.environ['API_ENV'] = 'test'

settings = get_settings()

app = app_generator()

args = {
    "app": "server.main:app",
    "host": "0.0.0.0",
    "port": 8000,
}

if settings.DEVELOP:
    args["reload"] = True

if __name__ == '__main__':
    uvicorn.run(**args)