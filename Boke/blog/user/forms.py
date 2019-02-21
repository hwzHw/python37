from django import forms


class UsersForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, label="姓名")
    age = forms.CharField(max_length=20, min_length=1, label="年龄")
    pwd = forms.CharField(max_length=255, min_length=1, label="密码", widget=forms.PasswordInput)