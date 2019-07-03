from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('view/<int:pk>', views.UserView.as_view(), name='user_view'),
    path('new', views.UserCreate.as_view(), name='user_new'),
    path('edit/<int:pk>', views.UserUpdate.as_view(), name='user_edit'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
]

