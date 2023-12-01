from django.shortcuts import render
from app import forms
# Create your views here.


# Create your views here.

def hello_view(request):
    form = forms.hello_name_forms(request.GET)
    if form.is_valid():
        user_name = form.cleaned_data["name"]
        return render(request,'hello.html', {"user_name": user_name})
    else:
        return render(request,'hello.html')
def age_in(request):
    form = forms.age_in_forms(request.GET)
    if form.is_valid():
        user_age = form.cleaned_data["age"]
        desired_year = form.cleaned_data["year"]
        total = desired_year - user_age
        return render(request,'age.html', {"A": user_age, "B": desired_year, "total": total})
    else:
        return render(request,'age.html')
def burger_view(request):
    form = forms.burger_forms(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = burgers * 4.50 + fries * 1.50 + drinks * 1 
        return render(request,'burger.html', {"total": total})
    else: 
        return render(request,'burger.html')