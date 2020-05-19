from .models import Avto, Marks, Mesto
from .serializers import AvtoSerializer, MarksSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthor
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

class AvtoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Avto.objects.select_related('cat_marka', 'cat_mesto')
    serializer_class = AvtoSerializer

class MarksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthor|ReadOnly]
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class MestoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Mesto.objects.all()
    serializer_class = MarksSerializer