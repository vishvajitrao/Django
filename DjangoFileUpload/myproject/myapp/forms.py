from django import forms
from .models import ProfileUpload,Cars,Document



class ProfileImage(forms.ModelForm):
    class Meta:
        model = ProfileUpload
        fields = ['Profile']
        


class CarUploadForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ('name','cars')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your favrouite car'}),
            'cars':forms.ClearableFileInput(attrs={'class':'form-control','multiple':True})
        }
    

class DocumentUpload(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['Doc']

