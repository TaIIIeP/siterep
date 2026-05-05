from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Форма реєстрації з обов'язковим полем Email
class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Електронна пошта")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# Форма для редагування профілю (Ім'я, Прізвище, Email)
class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="Ім'я")
    last_name = forms.CharField(max_length=30, required=False, label="Прізвище")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']