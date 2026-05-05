from django import imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Форма для реєстрації з обов'язковим Email
class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Вкажіть діючу пошту для відновлення пароля")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# Форма для оновлення імені та прізвища в кабінеті
class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="Ім'я")
    last_name = forms.CharField(max_length=30, required=False, label="Прізвище")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']