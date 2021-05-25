from product_models.class_serializers.product_serializers import ProductSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_management_models.product_stocks.models import ProductStock


class ProductStockSerializer(FlexFieldsModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductStock
        # exclude = ('removed_by',)
        fields = [
            'id',
            'product',
            'quantity'
        ]
        expandable_fields = {
            'product': ProductSerializer,
        }
