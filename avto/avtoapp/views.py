from django.shortcuts import render
from .models import Marks, Mesto, Avto
# Create your views here

avto_name = 'avtoapp'

def main_view(request):
    marks = Marks.objects.all()
    mesto = Mesto.objects.all()
    avto = Avto.objects.all()

    return render(request,'avtoapp/index.html', context={'marks': marks,
                                                         'mesto': mesto,
                                                         'avto': avto})

def create_post(request):
    return render(request, 'avtoapp/create.html')