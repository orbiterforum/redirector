import uuid
import json
from functools import lru_cache
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl

from .settings import settings
from .spaces import client
from .logger import logger


@lru_cache()
def get_json_data():
    """
    Load the JSON data into memory. It's cached into memory so it won't be re-loaded everytime.
    """
    temp_file_path = "/tmp/resources.json"

    # First we download the file from the space
    client.download_file(
        settings.space_name, settings.resource_json_location, temp_file_path
    )

    # Then we open and read it
    with open(temp_file_path, "r") as json_dump:
        json_data = json_dump.read()

    return json.loads(json_data)


def find_new_uri_by_id(id: uuid.UUID | int) -> HttpUrl:
    """
    Based on the passed id, determine if it's the old uuid or legacy id.
    Then look for this id in the lookup table and return the new uri if it exists.

    :param id: uuid.UUID | int
    :return: HttpUrl
    """
    if type(id) == uuid.UUID:
        search_key = "ohm_uuid"
        id = str(id)
    else:
        search_key = "legacy_id"

    for addon in get_json_data():
        if addon[search_key] == id:
            return addon["new_uri"]

    # If a request gets here, no match was found thus raising a 404.
    logger.error(f"Could not find {id} in the resources.json")
    raise HTTPException(404)


class UnifiedNotFoundResponse(RedirectResponse):
    """
    A RedirectResponse class, but with defaults set for this project.
    Will redirect to the URL defined in the `of_resource_url` setting and `not-found.92345788934758934` path.
    The redirect code will be the one specified in the `redirect_code` setting.
    """

    def __init__(self) -> None:
        super().__init__(
            f"{settings.of_resource_url}/not-found.92345788934758934",
            status_code=settings.redirect_code
        )
