from faker import Faker

from ..models import Item

from ..schema import ItemCreateModel


async def create_item(item: ItemCreateModel):
    """
    Create a new Item
    """
    fake = Faker()

    # Let's set the hidden field here
    ccn = fake.credit_card_number()

    return await Item.create(**{**item.dict(exclude_unset=True), "credit_card_number": ccn})
