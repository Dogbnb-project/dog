from django import forms
from django.contrib.auth.models import User
from dog.models import UserProfile
from dog.models import Cottage

###################################################
# ADD A COTTAGE
###################################################
class AddCottageForm(forms.ModelForm):

    class Meta:
        
        model = Cottage
        fields = ('name','region','sleeps','addr1','addr2','addr3','postcode','phone','price_from','price_to','picture')

###################################################
# CONTACT FORM
###################################################
class ContactForm(forms.Form):
    
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True,widget=forms.Textarea)

###################################################
# USER SIGN UP [base] [Page 111 of Rango Book]
###################################################
class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        
        model = User
        fields = ('username', 'email', 'password')

###################################################
# USER SIGN UP [extended user form]
###################################################
class UserProfileForm(forms.Form):

    # Drop down options for user types [admin not included!]
    USER_TYPES = (
        ('','-- select'),
        ('guest','Guest'),
        ('host','Host'),

    )
    
    usertype = forms.ChoiceField(required=True,choices=USER_TYPES, label="Guest / Host?") # drop down
    fname  = forms.CharField(required=True, label="First name") # text area
    lname  = forms.CharField(required=True, label="Last name") # text area
    bio  = forms.CharField(widget=forms.Textarea, required=True, label="About you") # text area
    picture  = forms.ImageField(required=True, label="Last name") # text area
