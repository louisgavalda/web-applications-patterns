from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from userauth.models import CustomUser


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=(
            "Djang does not stores password in readable form, So you cannot see"
            " this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")

    def clean_password(self):
        return self.initial["password"]


class CustomUserAddForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    def clean(self):
        super(CustomUserAddForm, self).clean()
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                {"password": "Passwords didn't match, Please enter again."}
            )
        else:
            pass

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        else:
            pass
        return user

    class Meta:
        model = CustomUser
        fields = "__all__"
