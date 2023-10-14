from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.forms import TextInput
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class UserForm(forms.ModelForm):
    """
    The default
    """
    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email']
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
            raise forms.ValidationError("email is taken")
        return email

    def save(self, commit=True):
        user = UserModel.objects.create_user_not_active_without_password(**self.cleaned_data)
        user.first_name = self.cleaned_data["user_first_name"]
        user.last_name = self.cleaned_data["user_last_name"]
        if commit:
            user.save()
        return user
