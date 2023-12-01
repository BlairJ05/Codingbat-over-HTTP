from django import forms

class Front_times(forms.Form):
    n = forms.IntegerField()
    input_str = forms.CharField(max_length=(100))
class no_teen_sum(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
class xyz_there(forms.Form):
    input_string = forms.CharField(max_length=100)
class centered_average(forms.Form):
    nums1 = forms.IntegerField()
    nums2 = forms.IntegerField()
    nums3 = forms.IntegerField()