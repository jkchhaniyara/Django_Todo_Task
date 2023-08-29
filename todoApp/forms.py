from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Todo


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(
        label="First Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    lastname = forms.CharField(
        label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.CharField(
        label="Email Address", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "firstname",
            "lastname",
            "username",
            "email",
            "password1",
            "password2",
        ]


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label="Title", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        label="Description",
        widget=forms.TextInput(attrs={"class": "form-control", "row": 5, "cols": 50}),
    )
    duedate = (
        forms.DateField(
            label="Due Date", widget=forms.DateInput(), input_formats=["%d-%m-%Y"]
        ),
    )
    completed = forms.BooleanField(
        label="Completed", widget=forms.CheckboxInput(), required=False
    )

    class Meta:
        model = Todo
        fields = ["title", "description", "duedate", "completed"]
