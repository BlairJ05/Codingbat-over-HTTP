from django.shortcuts import render
from app import forms
# Create your views here.
def front_times(request):
    form = forms.Front_times(request.GET)
    if form.is_valid():
        n = form.cleaned_data["n"]
        input_str = form.cleaned_data["input_str"]
        result = n * input_str[0:3]
        return render(request, 'front_times.html', {"form": form, "result": result})
    else:
        return render(request, 'front_times.html')

def no_teen_sum(request):
  form = forms.no_teen_sum(request.GET)
  if form.is_valid():
   a = form.cleaned_data["a"]
   b = form.cleaned_data["b"]
   c = form.cleaned_data["c"]
   if 13 <= a <= 19:
      if fix_teen(a):
         a = a
      else:
         a = 0
   if 13 <= b <= 19:
      if fix_teen(b):
         b = b
      else:
         b = 0
   if 13 <= c <= 19:
      if fix_teen(c):
         c = c
      else:
         c = 0
   result = a + b + c
   return render(request, 'no_teen_sum.html', {"result": result})
  else:
     return render(request, 'no_teen_sum.html')
def fix_teen(n):
   if n in {15, 16}:
      return (True)
  
def xyz_there(request):
   form = forms.xyz_there(request.GET)
   if form.is_valid():
      input_string = form.cleaned_data["input_string"]
      if "xyz" in input_string and ".xyz" not in input_string:
         result = True
      else:
         result = False
      return render(request, 'xyz_there.html', {"result":result, "forms":form})
   else:
      return render(request, 'xyz_there.html')
   
def centered_average(request):
    form = forms.centered_average(request.GET)
    if form.is_valid():
        nums1 = form.cleaned_data["nums1"]
        nums2 = form.cleaned_data["nums2"]
        nums3 = form.cleaned_data["nums3"]
        trim = sorted([nums1, nums2, nums3])[1:-1]
        result = sum(trim) / len(trim)
        return render(request, "centered_average.html", {"result": result, "form": form})
    else:
        return render(request, "centered_average.html")