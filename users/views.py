from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from users.forms import MiloUserForm
from users.models import MiloUser


class UserList(ListView):
    model = MiloUser


class UserView(DetailView):
    model = MiloUser


class UserCreate(CreateView):
    model = MiloUser
    form_class = MiloUserForm
    success_url = reverse_lazy('user_list')


class UserUpdate(UpdateView):
    model = MiloUser
    form_class = MiloUserForm
    success_url = reverse_lazy('user_list')


class UserDelete(DeleteView):
    model = MiloUser
    success_url = reverse_lazy('user_list')

