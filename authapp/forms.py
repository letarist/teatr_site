from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from authapp.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = User
        fields = ("username", "password")


class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'age')


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'age', 'password1', 'password2', 'email')
