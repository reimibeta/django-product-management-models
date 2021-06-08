import json

from datetime_utils.date_time import DateTime
from django.db.models import Sum, Case, When, F, DecimalField, Value, CharField, Avg, Count
from django.db.models.functions import TruncMonth, TruncDay
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_management_models.product_supplies.class_models.product_supply_stock import ProductSupplyStock
from product_management_models.product_supplies.class_serializiers.product_supply_stock_serializers import \
    ProductSupplyStockSerializer


class ProductSupplyStockViewSet(viewsets.ModelViewSet):
    queryset = ProductSupplyStock.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSupplyStockSerializer
