
from django import forms
from .models import  MyUser
from django.conf import settings
from django.core.mail import send_mail
from django.forms import CheckboxInput, ModelForm
from django.contrib.auth.forms import UserCreationForm
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, PasswordInput
from django.forms import Textarea, TextInput





class MyUserRegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields= ['username', 'email', 'password1', 'password2', ]
        widgets = {
            
            
            'username':TextInput(
                attrs={
                   "placeholder": "Enter name",
                   "class":"form-control",
                }
            ),
            'email':TextInput(
                attrs={
                   "placeholder": "Enter email",
                    "class":"form-control  form-label",
                }
            ),
            
            'password ':PasswordInput(
                attrs={
                  
                    "class":"form-control",
                }
            ),
             'password2':PasswordInput(
                attrs={
                  
                    "class":"form-control",
                }
            )
         }

class ProfileForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [ 'name', 'username', 'email',  'image', 'mobile_number', 'postcode',  'country', 'state', 'city', 'address']
        widgets = {
            'birth_date' : DatePickerInput(),
            
            'mobile_number':TextInput(
                
                attrs={
                    "placeholder": "Enter mobile no.",
                    "class":"form-control"
                }
            ), 
            'city':TextInput(
                
                attrs={
                    "placeholder": "Enter city.",
                    "class":"form-control"
                }
            ), 
            'state':TextInput(
                
                attrs={
                    "placeholder": "Enter state",
                    "class":"form-control"
                }
            ), 
            'country':TextInput(
                
                attrs={
                    "placeholder": "Enter country",
                    "class":"form-control"
                }
            ), 
            'postcode':TextInput(
                
                attrs={
                    "placeholder": "Enter postcode",
                    "class":"form-control"
                }
            ), 
             'address':Textarea(
                attrs={
                    "placeholder": "Enter your address",
                     "class":"form-control"
                }
            ),
            'name':TextInput(
                attrs={
                   "placeholder": "Enter name",
                   "class":"form-control"
                }
            ),
            
            'email':TextInput(
                attrs={
                   "placeholder": "Enter your email",
                   "class":"form-control"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter location name",
                   "class":"form-control"
                }
            )
           
            
        }
#Contact form
class ContactForm(forms.Form):

    name = forms.CharField(max_length=120, 
        widget=forms.TextInput(attrs={'placeholder': '*Your Full Name..', 'class':'form-control'}))
    phone = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': '*Your Phone No...', 'class':'form-control' }))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'placeholder': '*Your email..', 'class':'form-control'}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'placeholder': '*Your subject..',  'class':'form-control'}))
   
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '*Your Message..', 'class':'form-control'}))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )