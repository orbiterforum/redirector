import uuid

from redirector.utils import find_new_uri_by_id
from redirector.settings import settings
from .shared_data import client, id_to_test, uuid_to_test, resolved_uri


def test_get_addon_by_id():
    new_uri = find_new_uri_by_id(id_to_test)
    assert new_uri == resolved_uri

    response = client.get(f"/showAddon.php?id={id_to_test}")
    # Off while server is being readied
    # assert response.status_code == 307
    assert response.url == resolved_uri

    response = client.get(f"/showid.php?id={id_to_test}")
    # Off while server is being readied
    # assert response.status_code == 307
    assert response.url == resolved_uri


def test_get_addon_by_uuid():
    new_uri = find_new_uri_by_id(uuid.UUID(uuid_to_test))
    assert new_uri == resolved_uri

    response = client.get(f"/showAddon.php?id={uuid_to_test}")
    # Off while server is being readied
    # assert response.status_code == 307
    assert response.url == resolved_uri

    response = client.get(f"/showid.php?id={uuid_to_test}")
    # Off while server is being readied
    # assert response.status_code == 307
    assert response.url == resolved_uri


def test_get_addon_by_invalid_id():
    response = client.get("/showAddon.php?id=2378456278356237856")
    assert response.status_code == 404
    assert response.url == f"{settings.of_resource_url}/not-found.92345788934758934"
