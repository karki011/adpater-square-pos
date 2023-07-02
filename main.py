
from fastapi import FastAPI
from mangum import Mangum

from app.category import router as category_router

from app.locations import router as locations_router
from app.items import router as items_router
from app.category import router as category_router
from app.modifier_list import router as modifier_list_router

# from oauth import router as oauth_router

app = FastAPI()


@app.get("/health")
async def root():
    return {"message": "Hello From square adapater"}

app.include_router(locations_router, prefix="/locations")
app.include_router(items_router, prefix="/items")
app.include_router(category_router, prefix="/categories")
app.include_router(modifier_list_router, prefix="/modifier-list")
# app.include_router(oauth_router, prefix="/api")

handler = Mangum(app)
