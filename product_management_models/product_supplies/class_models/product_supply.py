from enum import Enum

from datetime_utils.date_time import DateTime
from django.db import models
from supplier_models.models import Supplier


# class ConditionChoice(Enum):
#     BUILD = "build"
#     SUPPLY = "supply"
#
#     @classmethod
#     def choices(cls):
#         return tuple((i.name, i.value) for i in cls)


class ProductSupply(models.Model):
    note = models.TextField(blank=True, null=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    request_date = models.DateField(default=DateTime('date').now())
    require_date = models.DateField(blank=True, null=True)
    supply_date = models.DateField(blank=True, null=True)
    # condition = models.CharField(
    #     choices=ConditionChoice.choices(),
    #     blank=True,
    #     null=True,
    #     max_length=120
    # )

    class Meta:
        verbose_name = 'Product supplies'
        verbose_name_plural = 'Product supplies'

    def __str__(self):
        return "{} (id:{})".format(self.request_date, self.id)
