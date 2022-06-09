from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import uuid
import pathlib

from .utils import find_new_uri_by_id, UnifiedNotFoundResponse
from .settings import settings

app = FastAPI()


@app.exception_handler(404)
async def handle_not_found(_, __) -> UnifiedNotFoundResponse:
    """
    404 NotFound handler.
    If a route is not found, the user will be redirected to the resources homepage
    """
    return UnifiedNotFoundResponse()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, __) -> UnifiedNotFoundResponse:
    """
    If the id query parameter is not an int or uuid, the validation will fail.
    In that case we will redirect the user to OF, instead of showing a json with the error.
    """
    return UnifiedNotFoundResponse()


@app.get("/showAddon.php")
@app.get("/showid.php")
async def redirect_to_resource(id: uuid.UUID | int) -> RedirectResponse:
    """
    A route that will redirect to the resource on OF based on the original UUID.
    If it can't find the id in the lookup table, it will redirect to the resources homepage.

    :param id: uuid.UUID | int
    :return: RedirectResponse
    """
    new_uri = find_new_uri_by_id(id)
    return RedirectResponse(new_uri, settings.redirect_code)


@app.get("/")
async def index():
    return RedirectResponse(settings.of_resource_url, status_code=settings.redirect_code)


# Mounting the staticfiles
app.mount("/", StaticFiles(directory=f"{pathlib.Path(__file__).parent.name}/static"), name="static")
