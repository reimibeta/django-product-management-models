from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_management_models.product_supplies.class_models.product_supply import ProductSupply
from product_management_models.product_supplies.class_models.product_supply_deliveries import ProductSupplyDelivery
from wallet_models.serializers import WalletSerializer


class ProductSupplyDeliverySerializer(FlexFieldsModelSerializer):
    # build = serializers.PrimaryKeyRelatedField(read_only=True)
    account = serializers.PrimaryKeyRelatedField(read_only=True)
    # order_build_workers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # supplier = serializers.PrimaryKeyRelatedField(read_only=True)
    # stock = serializers.PrimaryKeyRelatedField(read_only=True)
    delivery_cost = serializers.SerializerMethodField('delivery_cost_define')

    def delivery_cost_define(self, obj):
        return "{} {}".format(obj.cost_delivery, obj.account.currency.currency)

    supply = serializers.PrimaryKeyRelatedField(
        queryset=ProductSupply.objects.all(),
        write_only=True
    )

    class Meta:
        model = ProductSupplyDelivery
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'account',
            'supply',
            'deliver',
            'quantity',
            'delivery_cost',
            'delivery_date',
            'arrived_date',
            'payment_status',
            'delivery_status'
        ]
        expandable_fields = {
            'account': WalletSerializer,
            # 'stock': ProductStockSerializer,
            # 'supplier': SupplierSerializer,
            # 'product_build_worker': (ProductBuildWorkerSerializer, {'many': True}),
        }
