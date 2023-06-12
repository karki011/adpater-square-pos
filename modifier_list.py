# modifier_list.py
from typing import List, Optional, Union
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from square_client import client  # import the client

router = APIRouter()

class PriceMoney(BaseModel):
    amount: int
    currency: str


class ModifierData(BaseModel):
    name: str
    price_money: PriceMoney
    on_by_default: bool
    ordinal: int
    modifier_list_id: str


class Modifier(BaseModel):
    type: str
    id: str
    updated_at: str
    created_at: str
    version: int
    is_deleted: bool
    present_at_all_locations: bool
    present_at_location_ids: List[str]
    modifier_data: ModifierData


class ModifierListData(BaseModel):
    name: str
    ordinal: int
    selection_type: str
    modifiers: List[Modifier]
    is_conversational: bool


class ModifierList(BaseModel):
    type: str
    id: str
    updated_at: str
    created_at: str
    version: int
    is_deleted: bool
    present_at_all_locations: bool
    present_at_location_ids: List[str]
    modifier_list_data: ModifierListData


class Error(BaseModel):
    category: str
    code: str
    detail: str


@router.get("/", response_model=Union[List[ModifierList], Error])
def get_modifier_list():
    result = client.catalog.list_catalog(types='MODIFIER_LIST')

    if result.is_success():
        modifier_lists = []
        if 'objects' in result.body:
            for item in result.body['objects']:
                modifier_list_obj = ModifierList(**item)
                modifier_lists.append(modifier_list_obj)
        return modifier_lists
    else:
        error_details = []
        for error in result.errors:
            error_details.append(Error(
                category=error['category'],
                code=error['code'],
                detail=error['detail']
            ))
        return error_details

@router.get("/{id}", response_model=Union[ModifierList, Error])
def get_single_modifier_list(id: str):
    result = client.catalog.retrieve_catalog_object(object_id=id, include_related_objects=True)

    if result.is_success():
        if 'objects' in result.body:
            for item in result.body['objects']:
                if item['id'] == id:
                    return ModifierList(**item)
            raise HTTPException(status_code=404, detail="Modifier list not found")
        else:
            raise HTTPException(status_code=500, detail="No 'objects' key in response body")
    else:
        error_details = []
        for error in result.errors:
            error_details.append(Error(
                category=error['category'],
                code=error['code'],
                detail=error['detail']
            ))
        return {'error': error_details}