from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_management_models.product_stocks.serializers import ProductStockSerializer
from product_management_models.product_supplies.class_models.product_supply_stock import ProductSupplyStock
from supplier_models.supplier_serializers.supplier_serializers import SupplierSerializer
from wallet_models.serializers import WalletSerializer

class ProductSupplyStockSerializer(FlexFieldsModelSerializer):
    # build = serializers.PrimaryKeyRelatedField(read_only=True)
    account = serializers.PrimaryKeyRelatedField(read_only=True)
    # order_build_workers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    supplier = serializers.PrimaryKeyRelatedField(read_only=True)
    stock = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductSupplyStock
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
            'account',
            'supplier',
            'stock',
            'quantity',
            'price_per_unit',
            'is_transferred',
            'is_paid',
            'condition'
        ]
        expandable_fields = {
            'account': WalletSerializer,
            'stock': ProductStockSerializer,
            'supplier': SupplierSerializer,
            # 'product_build_worker': (ProductBuildWorkerSerializer, {'many': True}),
        }
