import uuid
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from pymongo import MongoClient
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


class CreateRiskEntry(APIView):
    def post(self, request):
        risk_id = request.data.get('risk_type')
        entry_data = request.data.get('entry_data')

        risk = RiskType.objects.get(id=risk_id)

        record = {}
        record['uuid'] = uuid.uuid4().__str__()
        
        for item in request.data.get('entry_data'):
            record[item] = entry_data.get(item).get('value')
     
        missing_required_fields = []

        fields_queryset = risk.fields.all()
        for field in fields_queryset:
            if field.is_required and not entry_data.get(field.name).get('value'):
                missing_required_fields.append(field.name)
        
        if missing_required_fields:
            return JsonResponse(
                {
                    'errors': {
                        'missing_fields': sorted(missing_required_fields)
                    }
                },
                status=500
            )

        client = MongoClient()
        database = client.insurance
        collection = database[risk.slug]

        collection.insert_one(record)

        return JsonResponse({'id': record['uuid']})
