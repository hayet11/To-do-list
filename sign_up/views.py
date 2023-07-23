from django.shortcuts import render , redirect
from .forms import sign_up_form

# Create your views here. 
def sign(request):
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = sign_up_form()
        
    return render(request,"sign.html",{"form": form})