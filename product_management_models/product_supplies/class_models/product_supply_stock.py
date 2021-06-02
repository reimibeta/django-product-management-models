from decimal import Decimal
from enum import Enum

from django.db import models
from django.db.models.signals import pre_save, post_delete, post_save, pre_delete
from django.dispatch import receiver

from supplier_models.models import Supplier
from wallet_models.class_models.wallet import Wallet

from product_management_models.class_projects.product_accounts.product_account_outlet import \
    product_account_outlet
from product_management_models.class_projects.product_stock.product_stock_supply import \
    product_stock_supply
from product_management_models.product_stocks.models import ProductStock
from product_management_models.product_supplies.class_models.product_supply import ProductSupply


class ConditionChoice(Enum):
    BUILD = "build"
    SUPPLY = "supply"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ProductSupplyStock(models.Model):
    account = models.ForeignKey(
        Wallet, on_delete=models.CASCADE
    )
    supply = models.ForeignKey(
        ProductSupply,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='product_supply_stock'
    )
    # order = models.ForeignKey(
    #     Order,
    #     on_delete=models.CASCADE,
    #     related_name='order_supply_stock',
    #     blank=True, null=True
    # )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    stock = models.ForeignKey(
        ProductStock,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    quantity = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00)
    )
    is_transferred = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=True)
    condition = models.CharField(
        choices=ConditionChoice.choices(),
        blank=True,
        null=True,
        max_length=120
    )

    class Meta:
        verbose_name = 'Product supply stocks'
        verbose_name_plural = 'Product supply stocks'

    def __str__(self):
        return "{}".format(self.stock)


@receiver(post_save, sender=ProductSupplyStock)
def add(sender, instance, created, **kwargs):
    if created:
        # stock
        product_stock_supply.supply_stock(current_instance=instance)
        # account
        product_account_outlet.outlet_account(
            instance,
            (instance.price_per_unit * instance.quantity)
        )


@receiver(pre_save, sender=ProductSupplyStock)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        old_value = ProductSupplyStock.objects.get(id=instance.id)
        product_stock_supply.update_stock(current_instance=instance, last_instance=old_value)
        # account
        product_account_outlet.update_outlet_account(
            instance, old_value,
            (instance.price_per_unit * instance.quantity),
            (old_value.price_per_unit * old_value.quantity)
        )


@receiver(pre_delete, sender=ProductSupplyStock)
def delete(sender, instance, using, **kwargs):
    # stock
    old_value = ProductSupplyStock.objects.get(id=instance.id)
    product_stock_supply.return_stock(last_instance=old_value)
    # account
    product_account_outlet.refund_outlet_account(
        old_value,
        (old_value.price_per_unit * old_value.quantity)
    )
