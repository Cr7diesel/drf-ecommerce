from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .product.views import CategoryView, BrandView, ProductView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
