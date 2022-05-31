import uuid
import json
from functools import lru_cache
from fastapi.exceptions import HTTPException
from pydantic import HttpUrl

from .settings import settings


@lru_cache()
def get_json_data():
    """
    Load the JSON data into memory. It's cached into memory so it won't be re-loaded everytime.
    """
    with open(settings.resource_mapping_json, "r") as json_dump:
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
    raise HTTPException(404)
