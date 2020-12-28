from rest_framework import serializers
from api_test.models import TestAPI

class TestAPISerializers(serializers.ModelSerializer):

  class Meta:
    model =  TestAPI
    fields = (
      'ticker',
      'day',
      'price',
    ) 