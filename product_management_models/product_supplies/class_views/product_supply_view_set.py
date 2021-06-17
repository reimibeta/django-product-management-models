import json

from django_datetime.datetime import datetime
from django.db.models import Sum, Case, When, F, DecimalField, Value, CharField, Avg, Count
from django.db.models.functions import TruncMonth, TruncDay
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_rest_framework.pagination import StandardResultsSetPagination

from product_management_models.product_supplies.class_models.product_supply import ProductSupply
from product_management_models.product_supplies.class_serializiers.product_supply_serializers import \
    ProductSupplySerializer


class ProductSupplyViewSet(viewsets.ModelViewSet):
    queryset = ProductSupply.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSupplySerializer


# product stock log
# class ProductSupplyLogViewSet(viewsets.ModelViewSet):
#     queryset = ProductSupplyLog.objects.order_by('-id').all()
#     pagination_class = StandardResultsSetPagination
#     serializer_class = ProductSupplyLogSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # IsAuthenticated, IsAuthenticatedOrReadOnly
#     authentication_classes = [JWTAuthentication, ]

# class ProductSupplyChartView(APIView):
#     def get(self, request):
#         objects = ProductSupply.objects
#         # date
#         if request.method == 'GET' and 'date' in request.GET:
#             # print(DateTime.parse_date(date).month)
#             if DateTime().is_date(request.GET['date']):
#                 date = datetime.parse_date(request.GET['date'])
#                 objects = objects.filter(date=date)
#         # month
#         if request.method == 'GET' and 'month' in request.GET:
#             # print(DateTime.parse_date(date).month)
#             if datetime.is_date(request.GET['month']):
#                 # month = DateTime.parse_date(request.GET['month'])
#                 objects = objects.filter(date__month=request.GET['month'])
#         # year
#         if request.method == 'GET' and 'year' in request.GET:
#             # print(DateTime.parse_date(date).month)
#             if datetime.is_date(request.GET['year']):
#                 # year = DateTime.parse_date(request.GET['year'])
#                 objects = objects.filter(date__year=request.GET['year'])
#         # supplier
#         if request.method == 'GET' and 'supplier' in request.GET:
#             objects = objects.filter(supplier=request.GET['supplier'])
#
#         data = objects.annotate(
#             supply_stock=F('stock__product__name')
#         ).values('supply_stock').annotate(
#             supply_qty=Sum('quantity')
#         ).annotate(
#             supply_cost=Sum(
#                 Case(
#                     When(currency__currency='USD', then=(F('cost_per_unit') / 1) * F('quantity')),
#                     default=((F('cost_per_unit') / float(4000)) * F('quantity')),
#                     output_field=DecimalField(),
#                 )
#             )
#         ).annotate(
#             supply_currency=Value('USD', CharField())
#         ).order_by('-stock')
#         # print(data)
#         return Response(data)
