from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

from accounts.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def is_valid(self):
        username = self.data.get('username')
        password = self.data.get('password')
        user = User.objects.filter(username__iexact=username).first()
        print(user)
        if user is None:
            self.add_error('username', 'Username does not exist')
            return False
        else:
            auth_user = auth.authenticate(username=username, password=password)
            if auth_user is None:
                self.add_error('password', 'Incorrect password')
                return False
            else:
                self.full_clean()
                return True


class RegisterForm(forms.ModelForm):
    # additional field to verify the password
    confirm_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    photo = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password',
            'photo'
        ]

    def is_valid(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        email = self.data.get('email')
        # Check the password
        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')
            return False
        else:
            # Check if email already exists
            if User.objects.filter(email=email).exists():
                self.add_error('email', 'Email already exits')
                return False
        self.full_clean()
        return True

    # With the default method the password is not hashed
    def save(self, commit=True):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['username']
        photo = self.cleaned_data['photo']
        profile = Profile()
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()
        profile.user = user
        profile.photo = photo
        profile.save()
        print(profile.photo)
        return user


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    def save(self, request, commit=True):
        user = request.user
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.email = self.data.get('email')
        user.profile.photo = self.data.get('photo')
        user.save()
        user.profile.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
