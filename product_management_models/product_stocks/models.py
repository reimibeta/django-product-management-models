from django.db import models
from product_models.class_models.product import Product


# product stocks
class ProductStock(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='product_stock',
        blank=True,
        null=True
    )
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(ProductStock, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.product)
