from product_models.class_serializers.product_serializers import ProductSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_management_models.product_stocks.models import ProductStock


# from product_models.class_projects.serializers.product_key_related_field import product_key_related_field

class ProductStockSerializer(FlexFieldsModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    # product = product_key_related_field.related_field()
    class Meta:
        model = ProductStock
        # exclude = ('removed_by',)
        fields = [
            'id',
            'product',
            'quantity',
            'is_available'
        ]
        expandable_fields = {
            'product': ProductSerializer,
        }
