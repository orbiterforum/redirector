from starlette import status

from .shared_data import client


def test_robots_txt():
    response = client.get("/robots.txt")
    assert response.status_code == status.HTTP_200_OK


def test_robots_txt_not_found():
    response = client.get("/robots.txt/demo")

    assert response.status_code == status.HTTP_404_NOT_FOUND
