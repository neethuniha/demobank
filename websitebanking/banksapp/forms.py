import json
from django import forms
from django.forms import ModelForm
from . models import User1,Branchs,Login

class UserAccountForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
    class Meta:
        model = Login
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            self.add_error('password_confirmation', "Password and confirmation do not match")

        return cleaned_data

class UserForm(forms.ModelForm):
    CHOICES = [
        ('Passbook', 'Passbook'),
        ('ATM Card', 'ATM Card')
        # Add more options as needed
    ]
    materials = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = User1
        fields = ['username', 'first_name', 'last_name', 'dob', 'phnno', 'email', 'gender', 'address','district','branch','ac_type','materials']
        widgets={
            'dob':forms.DateInput(attrs={'type':'date'}),
            'gender':forms.RadioSelect()
        }

    def clean_materials(self):
        # Convert list of choices to a string
        return ','.join(self.cleaned_data['materials'])


    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        branches_data = list(Branchs.objects.values('id', 'branch', 'district'))
        self.fields['branch'].widget = forms.Select()
        self.fields['branch'].queryset = Branchs.objects.none()

        # Include a JSON representation of the branches data for JavaScript
        self.branches_json = json.dumps(branches_data)

        # Populate the district dropdown
        self.fields['district'].widget = forms.Select(
            choices=[('', 'Select District')] + [(district, district) for district in
                                                 Branchs.objects.values_list('district', flat=True).distinct()])
        self.fields['username'].widget.attrs['readonly']=True

        if self.instance and self.instance.materials:
            self.fields['materials'].initial = self.instance.materials.split(',')



class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= Login
        fields=['username','password']