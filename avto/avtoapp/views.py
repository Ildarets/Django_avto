from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Marks, Mesto, Avto
from .forms import  ContactForm
from django.core.mail import send_mail
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['massage']
            send_mail('Тема письма',
                      message,
                      'ildarets@mail.ru',
                      [email],
                      fail_silently=True)
            return HttpResponseRedirect(reverse('avto_avito:index'))
        else:
            return render(request, 'avtoapp/create.html', context = {'form': form})
    else:
        form = ContactForm()
    return render(request, 'avtoapp/create.html', context = {'form': form})


def post(request, id):
    # post = Marks.objects.get(id=id)
    post = get_object_or_404(Avto, id = id)
    return render(request, 'avtoapp/post.html', context = {'post': post})

