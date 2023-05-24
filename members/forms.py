from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from .models import client,Invoice,Product,Usercompany, Userpayment,Number,Product1
class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(
            attrs={
                "class": "special",
                "size": "40",
                "label": "comment",
                "placeholder": "Username ",
            }))
    password = forms.CharField(label="",widget=forms.PasswordInput(
                               attrs={
                "class": "special",
                "size": "40",
                "label": "comment",
                "placeholder": "Password ",
            }))
class Addclient(forms.ModelForm):

    class Meta:
        model = client
        fields = ['companyname','companycode','vatcode','address','email']
        widgets = {
            'email': forms.EmailInput(
                               attrs={
                
                "size": "30",
                "class": "special",    
            }),
            'companyname': forms.TextInput(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
            'companycode': forms.TextInput(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
            'vatcode': forms.TextInput(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
            'address': forms.Textarea(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
        }

class saveinvoice(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['accountnumber','date','paydate','companyname','companycode','vatcode','address','email']
        widgets = {
            'accountnumber': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                
            }),
            'date': forms.DateTimeInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'paydate': forms.DateTimeInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'email': forms.EmailInput(
                               attrs={
                
                "size": "30",
                "class": "special",    
            }),
            'companyname': forms.TextInput(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
            'companycode': forms.TextInput(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
            'vatcode': forms.TextInput(
                               attrs={
                
                "size": "40",
                "class": "special", 
                
                
            }),
            'address': forms.Textarea(
                               attrs={
                
                "size": "40",
                "class": "special",
                
                
            }),
        }
class saveusercompany(forms.ModelForm):

    class Meta:
        model = Usercompany
        fields = ['name','phone','address','code','vat']
        widgets = {
            'name': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                
            }),
            'phone': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'address': forms.Textarea(
                               attrs={
                
                "size": "90",
                
               
            }),
            'code': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'vat': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
        }
class saveuserpayment(forms.ModelForm):

    class Meta:
        model = Userpayment
        fields = ['bankname','bankaccount','swift','vat']
        widgets = {
            'bankname': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                
            }),
            'bankaccount': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'swift': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'vat': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
        }
class product(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title','price','vat','quantity','totalprice','subtotal','tax','sumprice','sumtax','sumtotal']
        widgets = {
            'title': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                
            }),
            'price': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'quantity': forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'totalprice':forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'subtotal':forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
            'tax':forms.TextInput(
                               attrs={
                
                "size": "90",
                
               
            }),
        }

class product1(forms.ModelForm):

    class Meta:
        model = Product1
        fields = ['title','price','unit']
        widgets = {
            'title': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                
            }),
            'price': forms.TextInput(
                               attrs={
                
                "size": "90",
                
             
            }),
            'unit': forms.TextInput(
                               attrs={
                
                "size": "90",
                
             
            })
        }


   
class number1(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['quan']
        widgets = {
            'quan': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                "placeholder": " ",
            }),
            
        }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="",widget=forms.PasswordInput(
                               attrs={
                
                "size": "40",
                
                "placeholder": "Password ",
            }))

    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'email': forms.TextInput(
                               attrs={
                
                "size": "90",
               
                "placeholder": "Email ",
            }),
            'username': forms.TextInput(
                               attrs={
                
                "size": "90",
                
                "placeholder": "Username ",
            }),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
