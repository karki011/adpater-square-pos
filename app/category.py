from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from square_client import client  # import the client

router = APIRouter()


class Category(BaseModel):
    id: str
    name: str
    is_top_level: bool
    is_deleted: bool
    present_at_all_locations: bool


@router.get("/", response_model=List[Category])
def get_categories():
    result = client.catalog.list_catalog(types='CATEGORY')

    if result.is_error():
        error_details = [
            {
                'category': error['category'],
                'code': error['code'],
                'detail': error['detail']
            }
            for error in result.errors
        ]
        return {'error': error_details}

    categories: List[Category] = [
        Category(
            id=category['id'],
            name=category['category_data']['name'],
            is_top_level=category['category_data']['is_top_level'],
            is_deleted=category['is_deleted'],
            present_at_all_locations=category['present_at_all_locations']
        )
        for category in result.body['objects']
    ]

    return categories

@router.get("/{id}", response_model=Category)
def get_category(id: str):
    result = client.catalog.retrieve_catalog_object(object_id=id)

    if result.is_success():
        category = result.body['object']
        return Category(
            id=category['id'],
            name=category['category_data']['name'],
            is_top_level=category['category_data']['is_top_level'],
            is_deleted=category['is_deleted'],
            present_at_all_locations=category['present_at_all_locations']
        )
    else:
        error_details = [
            {
                'category': error['category'],
                'code': error['code'],
                'detail': error['detail']
            }
            for error in result.errors
        ]
        raise HTTPException(status_code=400, detail={'error': error_details})
