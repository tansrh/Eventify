from django.http import HttpResponse, HttpResponseRedirect
from models.models import Event, Attendee
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "home.html")
def loginn(request):
    if(request.method == "POST"):
        username=request.POST["username"]
        
        password=request.POST["password"]
        user=authenticate(username=username, password=password)
        if(user is not None):
            login(request, user)
            print(user)
            return render(request, "home.html")

        else:
            username=""

    return render(request, "login.html")
def logoutt(request):
    logout(request)
    
    return render(request, "home.html")
def register(request):
    if(request.method == "POST"):
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        if(password==confirm_password):
            try:
                
                newuser=User.objects.create_user(username,email,password)
                newuser.save()
                return render(request, "home.html")
            except:
                messages.success(request,"Failed")



    return render(request, "register.html")
def events(request):
    events=Event.objects.all().order_by('name')
    return render(request, "events.html", {'data': events})
def addevent(request):
    if(request.method=="POST"):

        eventName=request.POST['eventName']
        eventDescription=request.POST['eventDescription']
        eventDate=request.POST['eventDate']
        eventTime=request.POST['eventTime']
        eventLocation=request.POST['eventLocation']
        eventCapacity=request.POST['eventCapacity']
        en=Event(name=eventName, description=eventDescription, date=eventDate, time=eventTime, location=eventLocation, capacity=eventCapacity)
        en.save()
        return HttpResponseRedirect('/events')
    
    

    return render(request, "addevent.html")
def event(request, id):
    obj=""
    if(request.method=="GET"):
        obj = Event.objects.get(id = id)
    return render(request, "event.html", {"obj":obj})
def eventsregister(request, id):
    
    if(request.method=="GET"):
        obj = Event.objects.get(id = id)
        mail=request.user.email
        en=Attendee(name=obj.name, email=mail, event=obj)
        en.save()
        return HttpResponseRedirect('/events')
    return render(request, "event.html")

