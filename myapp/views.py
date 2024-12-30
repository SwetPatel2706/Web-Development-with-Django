from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html")

def AboutPage(request):
    return render(request, "about.html")

def ContactPage(request):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html")

def ParcelPage(request):
    return render(request, "parcel.html")

def LoadingPage(request):
    return render(request, "loading.html")

def myform(request):
    return render(request, "form.html")

def myformprocess(request):
    # print("Http Method is " + request.method)
    # print(request.POST)

    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    return render(request, "ans.html", {'mya':a, 'myb':b, 'myc':c})

