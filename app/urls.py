"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product-stocks/', include('product_management_models.product_stocks.urls')),
    path('api/product-supplies/', include('product_management_models.product_supplies.urls')),
    # supplier package module
    path('api/suppliers/', include('supplier_models.urls')),
    # product package module
    path('api/products/', include('product_models.urls')),
    # wallet package module
    path('api/wallets/', include('wallet_models.urls')),
    # user package module
    path('api/users/', include('user_models.urls')),
    # staff
    path('api/staffs/', include('staff_models.staffs.urls')),
    path('api/staff-groups/', include('staff_models.staff_groups.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
