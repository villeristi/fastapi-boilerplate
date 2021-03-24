from ..models import Item

from ..schema import ItemCreateModel


async def update_item(item_id: int, item: ItemCreateModel):
    """
    Update item
    """
    instance = await Item.get(pk=item_id)

    # Only .save() triggers auto_now on modified_at
    for k, v in item.dict(exclude_unset=True).items():
        setattr(instance, k, v)

    await instance.save()

    return instance
