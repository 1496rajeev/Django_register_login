from django import forms
from .models import Profile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email", "username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.PasswordInput()
        self.fields["password"].widget.attrs.update({"placeholder":"password"})
        self.fields["username"].widget.attrs.update({"placeholder":"username"})
        self.fields["email"].widget.attrs.update({"placeholder":"email"})
        self.fields["first_name"].widget.attrs.update({"placeholder":"name"})
        self.fields["last_name"].widget.attrs.update({"placeholder":"phone"})
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(max_length=4096, widget=forms.PasswordInput(attrs={'placeholder':'Your password'}))
