from django import forms

class age_in_forms(forms.Form):
    age = forms.IntegerField()
    year = forms.IntegerField()

class hello_name_forms(forms.Form):
    name = forms.CharField(max_length=(100))

class burger_forms(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()