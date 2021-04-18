from typing import Final, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from glypher.routes.main import router

origins: Final[List] = [
    'http://127.0.0.1/',
    'http://127.0.0.1:8081/',
    'http://localhost/',
    'http://localhost:8081/',
]


def make_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return app
