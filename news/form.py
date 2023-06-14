from django import forms

from news.models import newsData


class SignupForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control username','placeholder':'Username'}), max_length=50, required=True)
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}), max_length=50, required=True)
    emailid=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}), max_length=50, required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), max_length=16, required=True)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control username','placeholder':'Username'}), max_length=50, required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), max_length=16, required=True)

class update_news(forms.ModelForm):

    class Meta:
        model = newsData
        exclude=['user_id']
        
class Add_news(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control title','placeholder':'News Title'}), max_length=200, required=True)
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control content','placeholder':'News Content'}), max_length=1000, required=True)
    image=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control image','placeholder':'News Image'}),required=True)
    video=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control video','placeholder':'News Video'}),required=True)
