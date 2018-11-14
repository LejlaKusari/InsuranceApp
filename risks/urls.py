from django.urls import path
from .views import RetrieveRiskType, CreateRiskType, ListRiskType, CreateRiskEntry

urlpatterns = [
    path('<int:pk>/', RetrieveRiskType.as_view(), name='risk-detail'),
    path('create/', CreateRiskType.as_view(), name='risk-create'),
    path('list/', ListRiskType.as_view(), name='risk-list'),
    path('entry/', CreateRiskEntry.as_view(), name='risk-entry-create' )
]