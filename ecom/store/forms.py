from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Customize the 'username' field
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Enter your username",
                "class": "form-control",  # Add the 'form-control' class
            }
        )
        self.fields["username"].label = "Username"
        self.fields["username"].help_text = "Choose a unique username."
        self.fields["username"].error_messages = {
            "required": "Username is required.",
            "unique": "This username has already been taken.",
        }

        # Customize the 'first_name' field
        self.fields["first_name"].widget.attrs.update(
            {
                "placeholder": "Enter your first name",
                "class": "form-control",  # Add the 'form-control' class
            }
        )
        self.fields["first_name"].label = "First Name"
        self.fields["first_name"].help_text = "Please enter your first name."
        self.fields["first_name"].error_messages = {
            "required": "First name is required.",
        }

        # Customize the 'last_name' field
        self.fields["last_name"].widget.attrs.update(
            {
                "placeholder": "Enter your last name",
                "class": "form-control",  # Add the 'form-control' class
            }
        )
        self.fields["last_name"].label = "Last Name"
        self.fields["last_name"].help_text = "Please enter your last name."
        self.fields["last_name"].error_messages = {
            "required": "Last name is required.",
        }

        # Customize the 'email' field
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "Enter your email address",
                "class": "form-control",  # Add the 'form-control' class
            }
        )
        self.fields["email"].label = "Email Address"
        self.fields["email"].help_text = (
            "We'll never share your email with anyone else."
        )
        self.fields["email"].error_messages = {
            "required": "Email address is required.",
            "invalid": "Please enter a valid email address.",
        }

        # Customize the 'password1' field
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "Enter your password",
                "class": "form-control",  # Add the 'form-control' class
            }
        )
        self.fields["password1"].label = "Password"
        self.fields["password1"].help_text = (
            "Your password must contain at least 8 characters."
        )
        self.fields["password1"].error_messages = {
            "required": "Password is required.",
        }

        # Customize the 'password2' field (password confirmation)
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "Confirm your password",
                "class": "form-control",  # Add the 'form-control' class
            }
        )
        self.fields["password2"].label = "Confirm Password"
        self.fields["password2"].help_text = "Re-enter your password for confirmation."
        self.fields["password2"].error_messages = {
            "required": "Password confirmation is required.",
            "password_mismatch": "The two password fields didn’t match.",
        }
