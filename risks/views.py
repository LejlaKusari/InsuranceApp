from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import RiskType
from .serializers import RiskTypeSerializer
from .pagination_styles import StandardResultsPagination


class CreateRiskType(CreateAPIView):
    queryset = RiskType.objects
    serializer_class = RiskTypeSerializer


class RetrieveRiskType(RetrieveAPIView):
    queryset = RiskType.objects
    serializer_class = RiskTypeSerializer


class ListRiskType(ListAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
    pagination_class = StandardResultsPagination
