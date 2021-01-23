from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



PAYMENT_CHOICES = {
	('CD', 'Cash on Delivery(lipa mzigo ukiuona)')
}
class PaymentForm(forms.Form):
	payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class OrderNotesForm(forms.Form):
	order_notes = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 4
		}))
 
class RecivedForm(forms.Form):
	ref_code = forms.CharField()
	product = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 4
		}))


class pay(forms.Form):
	Order = forms.BooleanField()
	

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 4
		}))
	

WHAT_CHOICES = {
	('SWU', 'Sell With Us'),
	('DWU', 'Deliver With Us'),
	('MWU', 'Make Money With Us')
}

class SellForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField()
	phone = forms.CharField(max_length=100)
	option = forms.ChoiceField(widget=forms.RadioSelect, choices=WHAT_CHOICES)


class CommenttForm(forms.Form):
	subject = forms.CharField(max_length=100)
	comment = forms.CharField(max_length=300)
	rate = forms.IntegerField()




