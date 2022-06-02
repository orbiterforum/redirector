from fastapi.testclient import TestClient
import uuid

from redirector.main import app
from redirector.settings import settings
from redirector.utils import find_new_uri_by_id

client = TestClient(app)

# Shared test data
id_to_test = 6918
uuid_to_test = "7eb6850a-4e76-41ea-a6c3-c96e278956ca"
resolved_uri = "https://testforumapp.orbithangar.com/resources/mlm-update-for-mrm-module.5239/"


def test_robots_txt_happy_flow():
    response = client.get("/robots.txt")

    assert response.status_code == 200


# def test_robots_txt_not_found():
#     response = client.get("/robots.txt/demo")
#
#     # The response code will be 307 (or what's defined with `redirect_code`). It should redirect to OF.
#     assert response.status_code == settings.redirect_code
#     # assert response.url == f"{settings.of_resource_url}/not-found.92345788934758934"

def test_get_addon_by_id():
    new_uri = find_new_uri_by_id(id_to_test)
    assert new_uri == resolved_uri

    response = client.get(f"/showAddon.php?id={id_to_test}")
    assert response.status_code == 200


def test_get_addon_by_uuid():
    new_uri = find_new_uri_by_id(uuid.UUID(uuid_to_test))
    assert new_uri == resolved_uri

    response = client.get(f"/showAddon.php?id={uuid_to_test}")
    assert response.status_code == 200
