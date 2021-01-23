from django.forms import ModelForm, EmailInput, TextInput, FileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from User.models import UserProfile


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')
		widget = {
			'username' : TextInput(attrs={'class': 'input', 'placeholder':'username'}),
			'email': EmailInput(attrs={'class': 'input', 'placeholder':'email'}),
			'first_name': TextInput(attrs={'class': 'input', 'placeholder':'first_name'}),
			'last_name': TextInput(attrs={'class': 'input', 'placeholder':'last_name'})
		}

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('phone', 'image')
		widget = {
			'phone' : TextInput(attrs={'class': 'input', 'placeholder':'phone'}),
			'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'})
		}
