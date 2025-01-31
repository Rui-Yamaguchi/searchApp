from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={
        'required': 'メールアドレスを入力してください。',
        'invalid': '有効なメールアドレスを入力してください。',
    })

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        error_messages = {
            'username': {
                'required': 'ユーザー名を入力してください。',
                'unique': 'このユーザー名は既に使用されています。',
            },
            'password1': {
                'required': 'パスワードを入力してください。',
            },
            'password2': {
                'required': 'パスワード確認を入力してください。',
                'password_mismatch': 'パスワードが一致しません。',
            },
        }