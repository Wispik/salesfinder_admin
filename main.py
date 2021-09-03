from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/getcategories/{cat_id}")
async def getcategories(cat_id: int):
    if cat_id == 0:
        return data.catalog_items
    elif cat_id == 1:
        return data.catalog_items_1
    elif cat_id == 100:
        return data.catalog_items_10
    else:
        return HTTPException(404)