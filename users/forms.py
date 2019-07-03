from django import forms

from users import models


class MiloUserForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        exclude = ['random', 'date_joined', 'last_login']
        model = models.MiloUser


