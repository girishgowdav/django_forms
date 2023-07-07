from django import forms
g=[('male','MALE'),('female','FEMALE')]
class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
