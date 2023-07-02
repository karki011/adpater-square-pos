import os
from square.client import Client


access_token = os.environ.get('SQUARE_ACCESS_TOKEN')
environment = os.environ.get('SQUARE_ENVIRONMENT')

client = Client(
    access_token= 'EAAAEYTktKdSzgZI6rD5G9wcuhkbQLlwOvFsgngTnrgT-fuJZxHqUW-HR_qvJ9QM',
    environment= 'production'
)
