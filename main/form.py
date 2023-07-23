from django import forms

class NewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200, widget=forms.TextInput(attrs={'placeholder': 'The list\'s name'})) 
    # check = forms.BooleanField(required = False)
    # text = forms.CharField(label="Item", required= False, widget=forms.TextInput(attrs={'placeholder': 'Enter item here separated by "/"'}))
    

     