from .shared_data import client


def test_robots_txt():
    response = client.get("/robots.txt")
    assert response.status_code == 200


def test_robots_txt_not_found():
    response = client.get("/robots.txt/demo")

    # The response code will be 307 (or what's defined with `redirect_code`). It should redirect to OF.
    assert response.status_code == 404
