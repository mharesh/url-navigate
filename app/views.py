from django.shortcuts import render

# Create your views here.

def page(request):
    d={'name':'Dhoni','age':38,'hobbies':['cricket','kabbadi']}
    return render(request,'page.html',context=d)

def url(request):
    m={'a':10,'b':50}
    return render(request,'url.html',context=m)