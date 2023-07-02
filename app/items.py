from typing import List, Optional, Union
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from square_client import client  # import the client

router = APIRouter()

class PriceMoney(BaseModel):
    amount: int
    currency: str

class VariationData(BaseModel):
    item_id: str
    name: str
    ordinal: int
    pricing_type: str
    price_money: PriceMoney
    sellable: bool
    stockable: bool

class Variation(BaseModel):
    type: str
    id: str
    updated_at: str
    created_at: str
    version: int
    is_deleted: bool
    present_at_all_locations: bool
    item_variation_data: VariationData

class ItemData(BaseModel):
    name: str
    is_taxable: bool
    visibility: str
    category_id: Optional[str]
    variations: List[Variation]

class Item(BaseModel):
    type: str
    id: str
    updated_at: str
    created_at: str
    version: int
    is_deleted: bool
    present_at_all_locations: bool
    item_data: ItemData

class Error(BaseModel):
    category: str
    code: str
    detail: str

@router.get("/", response_model=Union[List[Item], Error])
def get_items():
    result = client.catalog.list_catalog(types='ITEM')

    if result.is_success():
        items = []
        if 'objects' in result.body:
            for item in result.body['objects']:
                items.append(Item(**item))
        return items
    else:
        error_details = []
        for error in result.errors:
            error_details.append(Error(
                category=error['category'],
                code=error['code'],
                detail=error['detail']
            ))
        return error_details

@router.get("/{id}", response_model=Union[Item, Error])
def get_item(id: str):
    result = client.catalog.retrieve_catalog_object(object_id=id, include_related_objects=True)

    if result.is_success():
        if 'object' in result.body:
            return Item(**result.body['object'])
        else:
            raise HTTPException(status_code=500, detail="No 'object' key in response body")
    else:
        error_details = []
        for error in result.errors:
            error_details.append(Error(
                category=error['category'],
                code=error['code'],
                detail=error['detail']
            ))
        return {'error': error_details}
