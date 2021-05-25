from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from staff_models.staffs.class_serializers.staff_serializers import StaffSerializer
from supplier_models.suppliers.supplier_serializers.supplier_serializers import SupplierSerializer

from product_management_models.product_stocks.serializers import ProductStockSerializer
from product_management_models.product_supplies.class_models.product_supply import ProductSupply


class ProductSupplySerializer(FlexFieldsModelSerializer):
    build = serializers.PrimaryKeyRelatedField(read_only=True)
    # order_build_workers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    supplier = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductSupply
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'stock',
            'supplier',
            'quantity',
            'date',
            'staff',
            'option',
            'is_transferred',
            'build',
            'note'
        ]
        expandable_fields = {
            'staff': StaffSerializer,
            'stock': ProductStockSerializer,
            'supplier': SupplierSerializer,
            # 'product_build_worker': (ProductBuildWorkerSerializer, {'many': True}),
        }
