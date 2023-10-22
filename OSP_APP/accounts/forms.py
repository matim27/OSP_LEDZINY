from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.forms import TextInput
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
UserModel = get_user_model()


class UserForm(forms.ModelForm):
    """
    The default
    """
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
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

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = UserModel.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Taki email jest już używany.")
        return email

    def save(self, commit=True):
        user = UserModel.objects.create_initial_user(**self.cleaned_data)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'})
        self.fields['username'].label = ""
        self.fields['password'].label = ""
