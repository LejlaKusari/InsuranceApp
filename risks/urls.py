from django.urls import path
from .views import RetrieveRiskType, CreateRiskType

urlpatterns = [
    path('<int:pk>', RetrieveRiskType.as_view(), name='risk-detail'),
    path('create', CreateRiskType.as_view(), name='risk-create'),
]