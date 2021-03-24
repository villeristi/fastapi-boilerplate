from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Item

ItemListModel = pydantic_model_creator(
    Item,
    name="ItemListModel",
    include=('id', 'name',),
)

ItemDetailModel = pydantic_model_creator(
    Item,
    name="ItemDetailModel",
    computed=("description",)
)

ItemCreateModel = pydantic_model_creator(
    Item,
    name="ItemCreateModel",
    exclude_readonly=True,
    exclude=("created_at", "modified_at",)
)
