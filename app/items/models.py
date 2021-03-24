from tortoise import fields, models


class Item(models.Model):
    """
    The Item model
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    catch_phrase = fields.CharField(max_length=255, null=True)

    # Will be exluded from results, visible only DB-level
    credit_card_number = fields.BigIntField()

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    # Computed value
    def description(self) -> str:
        """
        Returns the {name} - {catch_phrase}
        """
        return f"{self.name} - {self.catch_phrase}"

    class PydanticMeta:
        exclude = ["credit_card_number"]

    class Meta:
        table = "items"
