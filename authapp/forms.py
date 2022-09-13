from django.contrib.auth.forms import AuthenticationForm
from authapp.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'

    class Meta:
        model=User
        fields=('username','password')
