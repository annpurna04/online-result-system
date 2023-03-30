from django.shortcuts import render,redirect
from . models import students

# Create your views here.
def student(request):
    if request.session.get('rollno'):
        return redirect('shome')
    else:
        return render(request,'student.html') 

def slogin(request):
    rollno=request.POST['rollno']
    spass=request.POST['spass']
    
    res=students.objects.filter(rollno=rollno,spass=spass)
    
    if len(res)==1:
        request.session['rollno']=res[0].rollno
        return redirect('shome')
    else:
        return render(request,'student.html',{'error':'rollno or password incorrect!!!'})

def shome(request):
    if request.session.get('rollno'):
        return render(request,'shome.html')
    else:
        return redirect('/student/')
        
def smarks(request):
    res=students.objects.all()
    return render(request,'smarks.html',{'res':res})
    
def slogout(request):
    del request.session['rollno']
    return redirect('/student/')