from django.shortcuts import render,redirect
from twisted.words.protocols.jabber.component import Service

from .models import About,Education,Expericence,Services,Gallery,Client,Blog,Contact,Skill

# Create your views here.
def home(request):
    about=About.objects.all()
    education=Education.objects.all()
    expericence=Expericence.objects.all()
    service=Services.objects.all()
    gallery=Gallery.objects.all()
    client=Client.objects.all()
    blog=Blog.objects.all()
    skill=Skill.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        text=request.POST.get('text')
        contact=Contact(name=name,email=email,subject=subject,text=text)
        contact.save()
        return redirect('home')
    return render(request,'index.html',{"about":about,"education":education,"expericence":expericence,"service":service,"gallery":gallery,"client":client,"blog":blog,"skill":skill})