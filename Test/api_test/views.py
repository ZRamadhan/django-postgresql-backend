from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api_test.models import TestAPI
from api_test.serializers import TestAPISerializers
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def api_test_list(data):
    api_test = TestAPI.objects.all()

    if data.method == 'GET':
        api_test_serializers = TestAPISerializers(api_test, many=True)
        return JsonResponse(api_test_serializers.data, safe=False)

    # queryset = TestAPI.objects.all()
    # start_date = data.request.query_params.get('start_date', None)
    # end_date = data.request.query_params.get('end_date', None)
    # if start_date and end_date:
    #     queryset = queryset.filter(timstamp__range=[start_date, end_date])
    #     return JsonResponse(queryset.data, safe=False)
