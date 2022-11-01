from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def djangoform(request):
    NF=NameForm()
    d={'form':NF}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            n=form_data.cleaned_data['name']
            a=form_data.cleaned_data['age']
            pw=form_data.cleaned_data['password']
            d1={'name':n,'age':a,'password':pw}
            return render(request,'dispalyform.html',d1)
    return render(request,'djangoform.html',d)

def topic(request):
    T=Topicform()
    d={'topicform':T}
    if request.method=='POST':
        topic_data=Topicform(request.POST)
        if topic_data.is_valid():
            Tn=topic_data.cleaned_data['topic_name']
            d2={'topic_name':Tn}
            return HttpResponse('inserted in topic successfully')
    return render(request,'topic.html',d)

