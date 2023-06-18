
from fastapi import FastAPI
from mangum import Mangum

from category import router as category_router

from locations import router as locations_router
from items import router as items_router
from category import router as category_router
from modifier_list import router as modifier_list_router


app = FastAPI()


@app.get("/health")
async def root():
    return {"message": "Hello From square adapater"}

app.include_router(locations_router, prefix="/locations")
app.include_router(items_router, prefix="/items")
app.include_router(category_router, prefix="/categories")
app.include_router(modifier_list_router, prefix="/modifier-list")

handler = Mangum(app)
