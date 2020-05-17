from .models import Avto, Marks, Mesto
from .serializers import AvtoSerializer, MarksSerializer
from rest_framework import viewsets

class AvtoViewSet(viewsets.ModelViewSet):
    queryset = Avto.objects.select_related('cat_marka', 'cat_mesto').all()
    serializer_class = AvtoSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class MestoViewSet(viewsets.ModelViewSet):
    queryset = Mesto.objects.all()
    serializer_class = MarksSerializer