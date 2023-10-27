from django import forms
from django.contrib.auth import get_user_model
from django.forms import TextInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import DriverLicense, MedicalCheckup, SmokeBox, Training

UserModel = get_user_model()


class DriverLicenseForm(forms.ModelForm):
    class Meta:
        model = DriverLicense
        fields = ['category', 'permission_date', 'emergency_permission_date']
        widgets = {
            'permission_date': forms.DateInput(attrs={'type': 'text', 'placeholder': 'np. 19.10.2022'}),
            'emergency_permission_date': forms.DateInput(attrs={'type': 'text', 'placeholder': 'np. 19.10.2022'}),
            'category': forms.Select(),
        }
        labels = {
            'category': 'Rodzaj prawo jazdy',
            'permission_date': 'Data ważności prawo jazdy',
            'emergency_permission_date': 'Data ważności na pojazdy uprzywilejowane',
        }


class MedicalCheckupForm(forms.ModelForm):
    class Meta:
        model = MedicalCheckup
        fields = ['date', 'blood_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'text', 'placeholder': 'np. 19.10.2022'}),
            'blood_type': forms.TextInput(attrs={'type': 'text', 'placeholder': 'np. A  || Pole nie wymagane'}),
        }
        labels = {
            'date': 'Data ważności badań okresowych',
            'blood_type': 'Grupa krwi',
        }


class SmokeBoxForm(forms.ModelForm):
    class Meta:
        model = SmokeBox
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'text', 'placeholder': 'np. 19.10.2022'}),
        }
        labels = {
            'date': 'Data ważności komory dymowej',
        }


class TrainingForm(forms.ModelForm):
    TRAINING_CHOICES = (
        ('STRAŻAK', 'STRAŻAK'),
        ('DOWÓDCA', 'DOWÓDCA'),
        ('KIEROWCA', 'KIEROWCA'),
        ('KPP', 'KPP'),
        ('OWADY', 'OWADY'),
        ('RATOWNICTWO TECHNICZNE', 'RATOWNICTWO TECHNICZNE'),
    )

    training_name = forms.MultipleChoiceField(
        choices=TRAINING_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Wybierz posiadane szkolenia',
    )

    class Meta:
        model = Training
        fields = ['training_name']


class UserEditForm(forms.ModelForm):
    """
    The default
    """
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['phone_number'].label = ""

    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': 'Numer telefonu'}),
    )

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'first_name': TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': TextInput(attrs={'placeholder': 'Nazwisko'}),
        }
