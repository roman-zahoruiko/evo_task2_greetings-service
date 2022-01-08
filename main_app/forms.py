from django.forms import ModelForm
from .models import UserData


class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ["data"]

