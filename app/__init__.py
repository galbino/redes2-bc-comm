from fastapi import FastAPI
from app.utils.error_handler import generic_error
from app.utils.exceptions import AbroadException
from app.routers import *

tags_metadata = [
    {
        "name": "block",
        "description": "Routes that are used to communicate with the blocks from Blockchain's network."
    }
]


def create_app():

    app = FastAPI(
        openapi_tags=tags_metadata,
        title="Redes 2 - Blockchain Communication",
        description="This is an API made for the direct connection with the blockchain's network and to add and check blocks.",
        version="1.0.0"
    )

    app.include_router(health_router.router)
    app.include_router(block_router.router)

    app.add_exception_handler(AbroadException, generic_error)

    return app
