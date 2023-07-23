from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .form import NewList


# Create your views here.
def adding(t,TD):
    TD.item_set.create(text=t,complete= False)


def index(request,id):
        
    # items=l.item_set.get(id=1)
    # return HttpResponse("<html><body><h1>%s</h1><p>%s</p></body></html>" %(l,items))
    l= ToDoList.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("add"):
            txt = request.POST.get("textitem")
            if len(txt) > 0:
                adding(txt,l)
            else:
                print('invalid input!')
        elif request.POST.get("save"):
            for item in l.item_set.all():
                if request.POST.get('c'+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
    print(request.POST)
    return render(request,"list.html",{"l":l})


def home(request):
    todolist_names = request.user.todolist.all()
    return render(request,"home.html",{"list_name":todolist_names,})




def create(request):
    if(request.method == "POST"):
        form = NewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name= n)
            t.save()
            request.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = NewList()
    return render(request,"create.html",{"form":form})
