from rest_framework import (
    viewsets,
    permissions
    )

from services.models import (
	CloudService
	)

from .serializers import (
	CloudServiceSerializer
	)


class CloudServiceViewSet(viewsets.ModelViewSet):
	queryset = CloudService.objects.all()
	serializer_class = CloudServiceSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly)

