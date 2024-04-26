from rest_framework import viewsets
from .models import Exprementation,Result
from .serializers import ExprementationSerializer,ResultSerializer
# Create your views here.
class ExprementationViewSet(viewsets.ModelViewSet):
    queryset=Exprementation.objects.all()
    serializer_class=ExprementationSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset=Result.objects.all()
    serializer_class=ResultSerializer

