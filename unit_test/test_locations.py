import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient

from main import app
from app.locations import router as locations_router


client = TestClient(app)


@pytest.fixture
def locations_response():
    return {
        "locations": [
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
    }


def test_get_locations(locations_response):
    with patch("locations.client.locations.list_locations") as mock_list_locations:
        mock_list_locations.return_value.is_success.return_value = True
        mock_list_locations.return_value.body = locations_response

        response = client.get("/locations")

        assert response.status_code == 200
        response_json = response.json()

        expected_location = locations_response['locations'][0]
        actual_location = response_json[0]

        assert actual_location['id'] == expected_location['id']
        assert actual_location['name'] == expected_location['name']
        assert actual_location['address']['address_line_1'] == expected_location['address']['address_line_1']
        assert actual_location['address']['locality'] == expected_location['address']['locality']
        assert actual_location['address']['administrative_district_level_1'] == expected_location['address']['administrative_district_level_1']
        assert actual_location['address']['postal_code'] == expected_location['address']['postal_code']
        assert actual_location['address']['country'] == expected_location['address']['country']
        assert actual_location['timezone'] == expected_location['timezone']
        assert actual_location['capabilities'] == expected_location['capabilities']
        assert actual_location['status'] == expected_location['status']
        assert actual_location['created_at'] == expected_location['created_at']
        assert actual_location['merchant_id'] == expected_location['merchant_id']
        assert actual_location['country'] == expected_location['country']
        assert actual_location['language_code'] == expected_location['language_code']
        assert actual_location['currency'] == expected_location['currency']
        assert actual_location['phone_number'] == expected_location['phone_number']
        assert actual_location['business_name'] == expected_location['business_name']
        assert actual_location['type'] == expected_location['type']
        assert actual_location['website_url'] == expected_location['website_url']
        assert actual_location['business_hours'] == expected_location['business_hours']
        assert actual_location['business_email'] == expected_location['business_email']
        assert actual_location['coordinates'] == expected_location['coordinates']
        assert actual_location['logo_url'] == expected_location['logo_url']
        assert actual_location['pos_background_url'] == expected_location['pos_background_url']
        assert actual_location['mcc'] == expected_location['mcc']


if __name__ == "__main__":
    pytest.main()
