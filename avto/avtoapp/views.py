from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Marks, Mesto, Avto, Avto_pred
from .forms import ContactForm, PostForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here

avto_name = 'avtoapp'

def main_view(request):
    marks = Marks.objects.all()
    mesto = Mesto.objects.all()
    avto = Avto.objects.select_related('cat_marka', 'cat_mesto').all()
    paginator = Paginator(avto, 10)
    page = request.GET.get('page')
    try:
        avto = paginator.page(page)
    except PageNotAnInteger:
        avto = paginator.page(1)
    except EmptyPage:
        avto = paginator.page(paginator.num_pages)

    header = "главная страница"
    header_2 = "Список автомобилей, которые есть на сайте"

    return render(request,'avtoapp/index.html', context={'marks': marks,
                                                         'mesto': mesto,
                                                         'avto': avto,
                                                         'header': header,
                                                         'header_2': header_2})
@login_required
def contact_view(request):
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
            return render(request, 'avtoapp/contact.html', context = {'form': form})
    else:
        form = ContactForm()
    return render(request, 'avtoapp/contact.html', context = {'form': form})


def post(request, id):
    # post = Marks.objects.get(id=id)
    post = get_object_or_404(Avto, id = id)
    return render(request, 'avtoapp/post.html', context = {'post': post})

@login_required
def create_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'avtoapp/create.html', context = {'form':form})
    else:
        form = PostForm(request.POST, files = request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('avtoapp:index'))
        else:
            return render(request,'avtoapp/create.html', context = {'form':form})


class AvtoListView(ListView):
    model = Avto_pred
    template_name = 'avtoapp/avto_list.html'
    context_object_name = 'avto'
    paginate_by = 10

class AvtoDetailView(DetailView):
    model = Avto_pred
    template_name = 'avtoapp/post_detail.html'
    context_object_name = 'post_detail'

class AvtoCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Avto_pred
    success_url = reverse_lazy('avto:avto_list')
    template_name = 'avtoapp/create_avto.html'

class AvtoUpdateView(UpdateView):
    fields = '__all__'
    model = Avto_pred
    success_url = reverse_lazy('avto:avto_list')
    template_name = 'avtoapp/create_avto.html'

# Удаляет только суперпользователь
class AvtoDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'avtoapp/avto_delete_confirm.html'
    model = Avto_pred
    success_url = reverse_lazy('avto:avto_list')
    context_object_name = 'avto_delete'
    def test_func(self):
        return self.request.user.is_superuser



