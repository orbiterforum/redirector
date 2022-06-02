from fastapi.testclient import TestClient

from redirector.main import app

client = TestClient(app)

# Shared test data
id_to_test = 6918
uuid_to_test = "7eb6850a-4e76-41ea-a6c3-c96e278956ca"
resolved_uri = "https://testforumapp.orbithangar.com/resources/mlm-update-for-mrm-module.5239/"
