import importlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp

from . import settings


def get_asgi_application() -> ASGIApp:
    app_name: str = "Patron Criteria Exm"
    swagger_docs_url: str | None = None
    redoc_url: str | None = None

    if settings.DEBUG:
        swagger_docs_url = "/docs"
        redoc_url = "/redoc"

    app: ASGIApp = FastAPI(
        title=app_name,
        version=settings.VERSION,
        debug=settings.DEBUG,
        docs_url=swagger_docs_url,
        redoc_url=redoc_url,
        on_startup=[_startup_event],
    )

    _set_urls(app)
    _configure_cors(app)

    return app


def _startup_event() -> None:
    # start mappers
    from src.shared.primary_adapters.commands import start_sqlalchemy_mappers
    start_sqlalchemy_mappers()


def _set_urls(app: ASGIApp) -> None:
    for _app in settings.INSTALLED_APPS:
        app_urls = importlib.import_module(f"src.{_app}.adapters.api.views")

        if not hasattr(app_urls, "router"):
            raise Exception("missing router")  # MissingAPIRouterError()

        app_name: str | None = getattr(app_urls, "app_name", _app)
        app.include_router(app_urls.router, prefix=f"/{app_name}", tags=[app_name])


def _configure_cors(app: ASGIApp) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=settings.CORS_ALLOWED_METHODS,
        allow_headers=settings.CORS_ALLOWED_HEADERS,
    )
