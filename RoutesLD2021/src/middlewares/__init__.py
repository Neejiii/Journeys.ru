from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware
from settings import origins


def setup_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
