from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Donation, VolunteerApplication

class Registration (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'amount', 'credit_card_number']


class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'age', 'reasons_for_volunteering', 'skills']