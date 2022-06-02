from fastapi.exceptions import HTTPException
import pytest
import uuid

from redirector.utils import find_new_uri_by_id


def test_find_new_uri_by_id_with_fake_id():
    with pytest.raises(HTTPException):
        find_new_uri_by_id(284543653463)


def test_find_new_uri_by_id_with_fake_uuid():
    with pytest.raises(HTTPException):
        find_new_uri_by_id(uuid.UUID("3e9872d1-f992-4f17-af80-7f5969521508"))
