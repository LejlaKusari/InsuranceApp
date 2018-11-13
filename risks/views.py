from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import RiskType
from .serializers import RiskTypeSerializer


class CreateRiskType(CreateAPIView):
    queryset = RiskType.objects
    serializer_class = RiskTypeSerializer


class RetrieveRiskType(RetrieveAPIView):
    queryset = RiskType.objects
    serializer_class = RiskTypeSerializer
