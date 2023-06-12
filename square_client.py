import os
from square.client import Client

print(f"Square Access Token: {os.environ.get('environment')}")

access_token = os.environ.get('SQUARE_ACCESS_TOKEN')
environment = os.environ.get('SQUARE_ENVIRONMENT')

client = Client(
    access_token=access_token,
    environment=environment
)
