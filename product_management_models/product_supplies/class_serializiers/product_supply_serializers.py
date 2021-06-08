from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from supplier_models.supplier_serializers.supplier_serializers import SupplierSerializer

from product_management_models.product_stocks.serializers import ProductStockSerializer
from product_management_models.product_supplies.class_models.product_supply import ProductSupply
from product_management_models.product_supplies.class_serializiers.product_supply_stock_serializers import \
    ProductSupplyStockSerializer


class ProductSupplySerializer(FlexFieldsModelSerializer):
    # build = serializers.PrimaryKeyRelatedField(read_only=True)
    product_supply_stock = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # supplier = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductSupply
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            # 'stock',
            # 'supplier',
            # 'quantity',
            # 'date',
            # 'staff',
            # 'option',
            # 'is_transferred',
            # 'build',
            'note',
            'request_date',
            'require_date',
            'supply_date',
            'product_supply_stock'
        ]
        expandable_fields = {
            'product_supply_stock': ProductSupplyStockSerializer,
            # 'stock': ProductStockSerializer,
            # 'supplier': SupplierSerializer,
            # 'product_build_worker': (ProductBuildWorkerSerializer, {'many': True}),
        }
