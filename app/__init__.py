from fastapi import FastAPI
from app.utils.error_handler import generic_error
from app.utils.exceptions import AbroadException
from app.routers import *

tags_metadata = [
    {
        "name": "comm",
        "description": "Routes that are used to communicate with the Blockchain's network."
    }
]


def create_app():

    app = FastAPI(openapi_tags=tags_metadata)

    app.include_router(health_router.router)
    app.include_router(comm_router.router)

    app.add_exception_handler(AbroadException, generic_error)

    return app
