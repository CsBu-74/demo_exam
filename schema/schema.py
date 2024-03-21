from pydantic import BaseModel, ConfigDict
from typing import List


class ItemBase(BaseModel):
    # model_config = ConfigDict(from_attributes=True)
    title: str
    description: str
    category: str
    price: float
    discount: float | None
    quantity: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int


class SaleResponse(BaseModel):
    message: str
    items: List[Item]


class IncrementResponse(BaseModel):
    items: List[Item]