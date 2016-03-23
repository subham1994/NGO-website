from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UmeedUsers


class NewUserForm(ModelForm):
        username = forms.CharField(label=(u'Username'))
        email = forms.EmailField(label=(u'Email'))
        password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1 = forms.CharField(label=(u'Confirm Password'), widget=forms.PasswordInput(render_value=False))

        class Meta:
                model = UmeedUsers
                exclude = ('user', 'umeedId', 'coremember', 'isAdmin',)

        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError('username already taken !!')

        def clean(self):
                if self.cleaned_data.get('password') != self.cleaned_data.get('password1'):
                        raise forms.ValidationError('passwords do not match !!')
                return self.cleaned_data


class LoginForm(forms.Form):
        username = forms.CharField(label=(u'Username'))
        password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
