from django import forms

#django custom classes
class LoginForm(forms.Form):
    #it will generate html code from python dango form class

    # label=forms.FielType()
    # label=forms.FielType(label='')
    name=forms.CharField() #length is not required but in model it is required
    url = forms.URLField()
    email=forms.EmailField(required=True)

