from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uuid

from .utils import find_new_uri_by_id
from .settings import settings

app = FastAPI()


@app.exception_handler(404)
async def handle_not_found(_, __):
    """
    404 NotFound handler.
    If a route is not found, the user will be redirected to the resources homepage
    """
    return RedirectResponse(f"{settings.of_resource_url}/not-found.4", settings.redirect_code)


@app.get("/")
async def redirect_to_home() -> RedirectResponse:
    """
    Home route. Will redirect to the main resources module of OF.

    :return: RedirectResponse
    """
    return RedirectResponse(settings.of_resource_url, settings.redirect_code)


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
