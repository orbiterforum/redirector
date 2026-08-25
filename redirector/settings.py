from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redirect_code: int = 307
    of_resource_url: str = "https://testforumapp.orbithangar.com/resources"
    spaces_key: str
    spaces_secret: str
    spaces_endpoint: str = "https://nyc3.digitaloceanspaces.com"
    space_name: str = "ohm"
    resource_json_location: str = "resources/resources.json"


settings = Settings()
