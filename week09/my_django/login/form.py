from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

# def email_validate(value):
#     email_re = re.compile(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
#     if not email_re.match(value):
#         raise ValidationError("邮箱格式错误")

class LoginForm(forms.Form):
    email = forms.EmailField(
        # validators=[email_validate, ],
        label="邮箱", 
        widget=forms.widgets.TextInput(
            attrs={
                'type': "email", 
                "class": "form-control", 
                "placeholder": "Email",
                "id": "email"}))
    password = forms.CharField(
        min_length=8, 
        label="密码", 
        error_messages={'min_length': '密码长度最小8位'},
        widget=forms.widgets.PasswordInput(
            attrs={
                'type': 'password', 
                "class": "form-control", 
                "placeholder": "Password",
                "id": "password"}))
                
    # keep = forms.fields.ChoiceField(
    #     label="7天免登陆",
    #     initial="checked",
    #     widget=forms.widgets.CheckboxInput(attrs={"name": "is_check"})
    # )
