from ..models import Item


async def delete_item(item_id: int):
    """
    Delete item
    """

    return await Item.filter(id=item_id).delete()
