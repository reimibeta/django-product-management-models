from django.conf.urls import url
from django.urls import path, include
from product_management_models.product_supplies import views
from rest_framework import routers

router = routers.DefaultRouter()
""" Product supply api """
router.register('product-supply', views.ProductSupplyViewSet)
router.register('product-supply-stock', views.ProductSupplyStockViewSet)
router.register('product-supply-delivery', views.ProductSupplyDeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-supply-chart', views.ProductSupplyChartView.as_view())
]
