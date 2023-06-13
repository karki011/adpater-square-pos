from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter
from square.client import Client
from square_client import client

class Tax(BaseModel):
    id: str
    name: str
    calculation_phase: str
    inclusion_type: str
    percentage: str
    applies_to_custom_amounts: bool
    enabled: bool
    tax_type_id: str
    tax_type_name: str

class Address(BaseModel):
    address_line_1: str
    locality: str
    administrative_district_level_1: str
    postal_code: str
    country: str

class Location(BaseModel):
    id: str
    name: str
    address: Address
    timezone: str
    capabilities: List[str]
    status: str
    created_at: str
    merchant_id: str
    country: str
    language_code: str
    currency: str
    phone_number: str
    business_name: str
    type: str
    website_url: str
    business_hours: dict
    business_email: str
    coordinates: dict
    logo_url: str
    pos_background_url: str
    mcc: str
    tax: Optional[Tax]

router = APIRouter()

@router.get("/", response_model=List[Location])
def get_locations():
    print('get_locations')
    result = client.locations.list_locations()
    tax_result = client.catalog.list_catalog(types='TAX')

    if result.is_success() and tax_result.is_success():
        locations = []
        tax = None
        if 'objects' in tax_result.body and len(tax_result.body['objects']) > 0:
            tax_data = tax_result.body['objects'][0]['tax_data']
            tax = Tax(
                id=tax_result.body['objects'][0]['id'],
                name=tax_data['name'],
                calculation_phase=tax_data['calculation_phase'],
                inclusion_type=tax_data['inclusion_type'],
                percentage=tax_data['percentage'],
                applies_to_custom_amounts=tax_data['applies_to_custom_amounts'],
                enabled=tax_data['enabled'],
                tax_type_id=tax_data['tax_type_id'],
                tax_type_name=tax_data['tax_type_name']
            )

        for location in result.body['locations']:
            location_obj = Location(
                id=location['id'],
                name=location['name'],
                address=Address(
                    address_line_1=location['address']['address_line_1'],
                    locality=location['address']['locality'],
                    administrative_district_level_1=location['address']['administrative_district_level_1'],
                    postal_code=location['address']['postal_code'],
                    country=location['address']['country']
                ),
                timezone=location['timezone'],
                capabilities=location['capabilities'],
                status=location['status'],
                created_at=location['created_at'],
                merchant_id=location['merchant_id'],
                country=location['country'],
                language_code=location['language_code'],
                currency=location['currency'],
                phone_number=location['phone_number'],
                business_name=location['business_name'],
                type=location['type'],
                website_url=location['website_url'],
                business_hours=location['business_hours'],
                business_email=location['business_email'],
                coordinates=location['coordinates'],
                logo_url=location['logo_url'],
                pos_background_url=location['pos_background_url'],
                mcc=location['mcc'],
                tax=tax
            )
            locations.append(location_obj)
        return locations
    elif result.is_error():
        error_details = []
        for error in result.errors:
            error
