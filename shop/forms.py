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
	('S', 'Stripe'),
	('CD', 'Cash on Delivery')
}

Region = {
	('mwanza', 'mwanza'),
	('geita', 'geita')
}


class CheckoutForm(forms.Form):
	
	shipping_address = forms.CharField(required=False)

	shipping_address2 = forms.CharField(required=False)

	shipping_phone = forms.CharField(required=False)

	same_billing_address = forms.BooleanField(required=False)
	set_default_shipping = forms.BooleanField(required=False)
	use_default_shipping = forms.BooleanField(required=False)


	billing_address = forms.CharField(required=False)

	billing_address2 = forms.CharField(required=False)

	billing_phone = forms.CharField(required=False)

	same_billing_address = forms.BooleanField(required=False)
	set_default_shipping = forms.BooleanField(required=False)
	use_default_shipping = forms.BooleanField(required=False)
	set_default_billing = forms.BooleanField(required=False)
	use_default_billing = forms.BooleanField(required=False)

	
	payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

	region = forms.ChoiceField(choices=Region, label='Region(Mkoa)')


class OrderNotesForm(forms.Form):
	order_notes = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 4
		}))


class pay(forms.Form):
	Order = forms.BooleanField()
	
	
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField()
	phone = forms.CharField(max_length=100)
	massage = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 5
		}))


class CommenttForm(forms.Form):
	subject = forms.CharField(max_length=100)
	comment = forms.CharField(max_length=300)
	rate = forms.IntegerField()




