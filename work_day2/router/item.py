from fastapi import Body, APIRouter
from typing import Union, Optional
from pydantic import BaseModel
from config.database import db

class Item(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: Union[bool, None]

class ItemDetail(BaseModel):
    color: str
    detail: str


router = APIRouter(prefix="/items",
                   tags=["items"])


@router.get("/")
def root():
    return {"msg": "201"}


@router.get("/1/test")
def order():
    return {"msg": "order"}


@router.get("/{item_id}/{item_name}/{item_bool}")
def show_item(item_id: Union[int, str], item_name: str, item_bool: Union[bool, None]):
    print(type(item_id), type(item_name), type(item_bool))
    if item_bool is None:
        return {"item_id": item_id,
                "item_name": item_name}
    return {"item_id": item_id,
            "item_name": item_name,
            "item_bool": item_bool}


@router.post("/", status_code=201)
def create_item():
    return {"msg": f"create"}

#get(/items) default
@router.get("/")
def query_item(item_id: int = 1, item_name: str = "test", item_bool: Optional[bool] = None):
    if item_bool == None:
        return {"item_id": item_id,
                "item_name": item_name}
    return {"item_id": item_id,
            "item_name": item_name,
            "item_bool": item_bool}


@router.get("/body")
def show_item_body(item: Item, item_detail: ItemDetail):
    return {"item": item, "detail": item_detail}


#HTTP look item_color as parameter not body need to use ? to pass parameter
@router.get("/body_with_para")
def show_body_para(item: Item, item_color: str):
    return {"item": item, "color": item_color}


@router.get("/body_with_para_body")
def show_body_para(item: Item, item_color: str = Body()):
    return {"item": item, "color": item_color}


@router.get("/{stdId}")
def show_enroll(stdId: int):
    collection = db['exceed11']
    list_data = []
    for item in collection.find({"stdId": stdId}, {'_id': 0}):
        list_data.append(item)
    return {'data': list_data}