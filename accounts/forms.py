from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)

    def is_valid(self):
        username = self.data.get('username')
        password = self.data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            self.add_error('password','User does not exist')
            return False
        else:
            self.full_clean()
            return True

class RegisterForm(forms.ModelForm):
    # additional field to verify the password
    password2 = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
        ]

    def is_valid(self):
        password = self.data.get('password')
        password2 = self.data.get('password2')
        email = self.data.get('email')
        # Check the password
        if password != password2:
            self.add_error('password2', 'Passwords do not match')
            return False
        else:
            # Check the email already exists
            if User.objects.filter(email=email).exists():
                self.add_error('email','Email already exits')
                return False
        self.full_clean()
        return True
