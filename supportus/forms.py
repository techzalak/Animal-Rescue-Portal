from django import forms
'''
Favchoice=[
    (False,'Make this an anonymous donation'),
]
'''

class donateform(forms.Form):
    name = forms.CharField(label="Name*",widget=forms.TextInput(attrs={'placeholder':'Enter your name','class':'textbox2'}))
    email = forms.EmailField(label="Email*",widget=forms.EmailInput(attrs={'placeholder':'Enter your email address','class':'textbox2'}))
    mobile = forms.CharField(label="Mobile No*", min_length=10 , max_length=10 , widget=forms.TextInput(attrs={'placeholder':'Enter your mobile no','class':'textbox2'}))
    comment= forms.CharField(label="Comment", widget=forms.Textarea(attrs={'placeholder':'Leave a comment','class':'textarea'}))
    add = forms.CharField(label="Address",widget=forms.TextInput(attrs={'placeholder':'Enter your address','class':'textbox2'}))
    #state = forms.CharField(label="State",widget=forms.TextInput(attrs={'placeholder':'Enter your state','class':'textbox2'}))
    #checkvar=forms.MultipleChoiceField(label=" ",label_suffix=False,required=False,widget=forms.CheckboxSelectMultiple(attrs={'class':'textbox3'}),choices=Favchoice)
    anony = forms.CharField(label="Make this an Anonymous donation?",widget=forms.TextInput(attrs={'placeholder':'Yes/No','class':'textbox2'}))