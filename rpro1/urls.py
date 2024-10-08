from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.PersonViewset import PersonViewSet
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
