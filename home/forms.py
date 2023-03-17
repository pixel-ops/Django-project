from django import forms
from django.forms import ModelForm
from .models import myabout,mypost,mycontact,myregister,multiple_images
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
class aboutcontact(forms.ModelForm):
    
    
    
    class Meta:
        model = mycontact
        fields = ("name","password","address1","address2","city","state","zip")
        
        widgets = {
            "name": forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter your name"}),
            "password":forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter your password"}),
            "address1":forms.Textarea(attrs={"style": " height:10px;",'class':'form-control',"placeholder":"Enter your address"}),
            "address2":forms.Textarea(attrs={"style": "height:10px;",'class':'form-control',"placeholder":"Enter your address"}),
            "city":forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter your city"}),
            "state":forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter your state"}),
            "zip":forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter your zip"}),
        }


def is_anagram(x,y):
    return sorted(x) == sorted(y)

class aboutform(ModelForm):
    
    class Meta:
        model = myabout
        fields = ("userid","first_name","last_name","phone","email","address","extra")
       
        widgets = {
            "first_name": forms.TextInput( attrs={"style": "width: 800px;",'class':'form-control',"placeholder":"Enter your name"}),
            "last_name": forms.TextInput(attrs={"style": "width: 800px;",'class':'form-control',"placeholder":"Enter your last name"}),
            "phone": forms.TextInput(attrs={"style": "width: 800px;",'class':'form-control',"placeholder":"Enter your Phone number"}),
            "email": forms.EmailInput(attrs={"style": "width: 800px;",'class':'form-control',"placeholder":"Enter your email"}),
            "address": forms.Textarea(attrs={"style": "width: 800px;",'class':'form-control',"placeholder":"Enter your address"})
        }

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if not is_anagram(data,'silent'):
            raise forms.ValidationError("The string is not anagram")
        return data


class aboutpost(ModelForm):
    class Meta:
        model = mypost
        fields = ("topic","author","content","content_type","genre","img")

        widgets = {
            "topic": forms.TextInput( attrs={"style": "",'class':'form-control',"placeholder":"Enter your topic"}),
            "author": forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter author name"}),
            "content": forms.Textarea(attrs={"style": "height:100px",'class':'form-control',"placeholder":"Enter your content"}),
            "content_type": forms.TextInput(attrs={"style":"",'class':'form-control',"placeholder":"Enter your content type"}),
            "genre": forms.TextInput(attrs={"style": "",'class':'form-control',"placeholder":"Enter your genre"}),
            "img": forms.FileInput(attrs={"style":"",'class':'form-control',"placeholder":"Enter your genre"})
        }

class aboutregister(ModelForm):
    class Meta:
        model = myregister
        fields = ("user_name","user_email","user_password","user_location","user_number")

    def save(self, user=None):
        user_profile = super(aboutregister, self).save(commit=False)
        if user:
             user_profile.user = user
             user_profile.save()
             return user_profile
        
class aboutmultipleimage(ModelForm):
    class Meta:
        model = multiple_images
        fields = ("post","image")

        # widgets = {
        #     # "post": forms.TextInput( attrs={"style": "",'class':'form-control',"placeholder":"Enter your topic"}),
        #     "image": forms.FileInput(attrs={"style":"",'class':'form-control',"placeholder":"Enter your genre"})
        # }