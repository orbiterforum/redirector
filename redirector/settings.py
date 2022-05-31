from pydantic import BaseSettings, HttpUrl
from pydantic.types import FilePath


class Settings(BaseSettings):
    redirect_code: int = 307
    of_resource_url: HttpUrl = "https://testforumapp.orbithangar.com/resources"
    resource_mapping_json: FilePath = "./resources.json"


settings = Settings()
