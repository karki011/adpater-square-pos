

# Square Adapter API

The Square Adapter API provides an API layer using the Square SDK to interact with Square's services. It exposes endpoints for various resources such as locations, items, categories, and modifier lists.

## Endpoints

The following endpoints are available in the Square Adapter API:

### Locations

- **GET /locations**: Retrieve a list of locations.
  - Returns a list of all locations.
  - Example response:
    ```json
    [
      {
        "id": "LSZ3FTP9ZY60P",
        "name": "Krazy Curry",
        "address": {
          "address_line_1": "500 W Summit Ave",
          "locality": "Charlotte",
          "administrative_district_level_1": "NC",
          "postal_code": "28203",
          "country": "US"
        },
        "timezone": "America/New_York",
        "capabilities": [
          "CREDIT_CARD_PROCESSING",
          "AUTOMATIC_TRANSFERS"
        ],
        "status": "ACTIVE",
        "created_at": "2021-12-25T16:32:15.165Z",
        "merchant_id": "MLKSF4ZBCWRV5",
        "country": "US",
        "language_code": "en-US",
        "currency": "USD",
        "phone_number": "+1 704-728-0244",
        "business_name": "Krazy Curry",
        "type": "PHYSICAL",
        "website_url": "https://www.krazycurry.com/",
        "business_hours": {},
        "business_email": "info@krazycurry.com",
        "coordinates": {
          "latitude": 35.220067,
          "longitude": -80.860688
        },
        "logo_url": "https://square-web-production-f.squarecdn.com/files/09930df7c491e505bd263ba96122e318845ba775/original.jpeg",
        "pos_background_url": "https://square-web-production-f.squarecdn.com/files/7ffdde6dcec898cb4457be158e88095760eff47b/original.jpeg",
        "mcc": "5812"
      }
    ]
    ```
  - Status code: 200 (OK)

### Items

- **GET /items**: Retrieve a list of items.
- **GET /items/{item_id}**: Retrieve information about a specific item.

### Categories

- **GET /categories**: Retrieve a list of categories.
- **GET /categories/{category_id}**: Retrieve information about a specific category.

### Modifier Lists

- **GET /modifier-lists**: Retrieve a list of modifier lists.
- **GET /modifier-lists/{modifier_list_id}**: Retrieve information about a specific modifier list.

## Square Client Configuration

The Square SDK requires valid credentials and configuration to connect to your Square account. To configure the Square client, open the `square._client.py` file and update the `Client` configuration as follows:

```python
from square.client import Client

client = Client(
    access_token='EAAAneMQ9ERBE35u45Q0C2FVx79jkbn2rU65a7Wn42k',
    environment='production'
)
```

Make sure to replace the `access_token` with your own Square access token.

## Getting Started

To run the Square Adapter API locally, follow these steps:

1. Clone the repository: `git clone https://github.com/

your-repo/square-adapter-api.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the necessary configuration and environment variables for the Square SDK.
4. Run the API: `python main.py`

Ensure that you have valid credentials and configuration for the Square SDK to connect to your Square account.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

Please make sure to follow the code style guidelines and include appropriate tests for your changes.

## License

This project is licensed under the [MIT License](LICENSE).
