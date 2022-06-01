from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    redirect_code: int = 307
    of_resource_url: HttpUrl = "https://testforumapp.orbithangar.com/resources"
    spaces_key: str
    spaces_secret: str
    spaces_endpoint: HttpUrl = "https://nyc3.digitaloceanspaces.com"
    space_name: str = "ohm"
    resource_json_location: str = "resources/resources.json"


settings = Settings()
