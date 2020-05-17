from django.conf.urls import url, include
from .models import Avto, Marks, Mesto
from rest_framework import routers, serializers, viewsets

class AvtoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avto
        fields = '__all__'

class MarksSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'

class MestoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mesto
        fields = '__all__'