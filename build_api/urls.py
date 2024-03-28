
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import KontakViewset

router = routers.DefaultRouter()
router.register('kontak', KontakViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
