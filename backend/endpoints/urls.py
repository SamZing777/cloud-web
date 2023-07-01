from django.urls import path, include
from rest_framework import routers

from .views import (
	CloudServiceViewSet
	)

router = routers.DefaultRouter()
router.register('service', CloudServiceViewSet)

urlpatterns = router.urls
