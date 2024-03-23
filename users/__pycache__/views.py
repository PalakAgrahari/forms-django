from django.http import HttpResponse
from django.shortcuts import render
# from palak.models import signin
from django.urls import path
def homePage(request):
    data = {
       'title':'Home wdh',
       'clist':['PHP','Java','Python'],
       'cnum':[10,23,56]
    }
    return render(request,"intro.html",data)

def Details(request):
    # if request.method == "POST":
    #     name = request.POST.get('fname')
    #     username =  request.POST.get('uname')
    #     password = request.POST.get('pass')
    #     en = signin(name=name,username=username,password=password)
    #     en.save()
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Wlcome to my website")

def courseDetails(request,courseid):
    return HttpResponse(courseid)