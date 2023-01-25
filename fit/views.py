from fit.serializers import FitSerializer
from fit.models import Fit
from rest_framework.viewsets import ModelViewSet

class FitViewSet(ModelViewSet):
    queryset = Fit.objects.all()
    serializer_class = FitSerializer
