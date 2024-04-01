from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from webapp.api.robot_control.router import robot_router
from webapp.integrations.logger import init_logger


def setup_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def setup_routers(app: FastAPI) -> None:
    app.include_router(robot_router)


def create_app() -> FastAPI:
    app = FastAPI(docs_url='/swagger')
    setup_middleware(app)
    setup_routers(app)
    init_logger('API')
    init_logger('Robot')

    return app
