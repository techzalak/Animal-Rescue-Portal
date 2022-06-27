from django import forms
from django.core.exceptions import ValidationError
Pet_choices=[
    ('dog','Dog',),
    ('cat','Cat'),
    ('bird', 'Bird'),
    ('cow','Cow')
]
class RescueDetails(forms.Form):
    name = forms.CharField(label="Name*",widget=forms.TextInput(attrs={'placeholder':'Enter your name','class':'textbox'}))
    mobile = forms.CharField(label="Mobile No*", min_length=10 , max_length=10 , widget=forms.TextInput(attrs={'placeholder':'Enter your mobile no','class':'textbox'}))
    animal =forms.CharField(label="Type of Animal*", widget=forms.Select(choices=Pet_choices, attrs={'class':'textbox'}))
    img = forms.ImageField(label="Add Image*",  required=False, widget=forms.FileInput(attrs={'class':'textbox'}))
    strt = forms.CharField(label="Street",widget=forms.TextInput(attrs={'placeholder':'Enter street name','class':'textbox1'}))
    lama = forms.CharField(label="Landmark",widget=forms.TextInput(attrs={'placeholder':'Enter any landmark','class':'textbox1'}))
    city = forms.CharField(label="City",widget=forms.TextInput(attrs={'placeholder':'Enter city ','class':'textbox1'}))
    state = forms.CharField(label="State",widget=forms.TextInput(attrs={'placeholder':'Enter state','class':'textbox1'}))
    pin = forms.CharField(label="Pincode",min_length=6,max_length=6,widget=forms.TextInput(attrs={'placeholder':'Enter pincode','class':'textbox1'}))
    def clean_pin(self):
        valname = self.cleaned_data['pin']
        if(len(valname) != 6 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid pin code of 6 digits')
        return valname
    def clean_mobile(self):
        valname = self.cleaned_data['mobile']
        if(len(valname) != 10 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid mobile number of 10 digits')
        return valname