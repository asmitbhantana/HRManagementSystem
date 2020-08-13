from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField()

    class Meta:
        fields = ['username', 'password']


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('This email is already Register!')
        return self.cleaned_data['email']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('This username is already taken!')
        return self.cleaned_data['username']

    def clean(self):
        print(self.cleaned_data)
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords doesn\'t matches!')

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]