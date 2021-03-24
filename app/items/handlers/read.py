from ..models import Item


async def list_items():
    """
    Display a list of items
    """
    return await Item.all()


async def get_item(item_id: int):
    """
    Display a single item
    """
    return await Item.get(pk=item_id)
