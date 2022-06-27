from django import forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Signupclass
class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'textfield'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'textfield'}))

class sign(UserCreationForm):
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter password','class':'textfield2'}), help_text="")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'textfield2'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email','class':'textfield2'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your first name','class':'textfield2'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name','class':'textfield2'}))
    mobile = forms.CharField(label="Mobile No", min_length=10 , max_length=10 , widget=forms.TextInput(attrs={'placeholder':'Enter your mobile no','class':'textfield2'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your address','class':'textfield2'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'textfield2'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name' ,'last_name','mobile','address','email','password1','password2']
        help_texts = {
            'username': None,
            'password1':"",
            'password2':"",
       
        }
class Edit(UserChangeForm):
    password = None
    password1 = None
    password2 = None
    username=forms.CharField(widget=forms.TextInput(attrs={'readonly':True}))
    class Meta:
        model = User
        fields =['username','first_name', 'last_name', 'email']
class addEdit(Edit):
    password = None
    username = None
    class Meta:
        model = Signupclass
        fields =['address', 'mobile']
class Address(addEdit):
    strt = forms.CharField(label="Street",widget=forms.TextInput(attrs={'placeholder':'Enter street name','class':'textbox1'}))
    lama = forms.CharField(label="Landmark",widget=forms.TextInput(attrs={'placeholder':'Enter any landmark','class':'textbox1'}))
    city = forms.CharField(label="City",widget=forms.TextInput(attrs={'placeholder':'Enter city ','class':'textbox1'}))
    state = forms.CharField(label="State",widget=forms.TextInput(attrs={'placeholder':'Enter state','class':'textbox1'}))
    pin = forms.CharField(label="Pincode",widget=forms.TextInput(attrs={'placeholder':'Enter pincode','class':'textbox1'}))
    class Meta:
        model = Signupclass
        fields =['strt', 'lama', 'city', 'state', 'pin']