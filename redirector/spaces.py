import boto3

from .settings import settings

session = boto3.session.Session()
client = session.client(
    "s3",
    # region_name is just a placeholder: https://docs.digitalocean.com/products/spaces/resources/s3-sdk-examples/
    region_name="nyc3",
    endpoint_url=settings.spaces_endpoint,
    aws_access_key_id=settings.spaces_key,
    aws_secret_access_key=settings.spaces_secret,
)
