from django import forms

from users import models


class MiloUserForm(forms.ModelForm):

    class Meta:
        exclude = ['random', 'date_joined', 'last_login']
        model = models.MiloUser


