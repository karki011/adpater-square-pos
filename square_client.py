import os
from square.client import Client


access_token = os.environ.get('SQUARE_ACCESS_TOKEN')
environment = os.environ.get('SQUARE_ENVIRONMENT')

client = Client(
    access_token='EAAAEQzgzmAXkoxcL2KURsjZPf8aEOKyRz3x9X5_bcgZv1ABEowTeY9nEqyTxg3Q',
    environment='production'
)
