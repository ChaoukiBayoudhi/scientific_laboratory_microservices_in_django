from rest_framework import serializers
from .models import Exprementation,Result
class ExprementationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exprementation
        fields='__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields='__all__'