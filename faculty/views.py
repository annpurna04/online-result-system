from django.shortcuts import render,redirect
from . models import faculty_login 
from student.models import students

# Create your views here.

def faculty(request):
    if request.session.get('fuser'):
        return redirect('home')
    else:
        return render(request,'faculty.html')
    
def flogin(request):
    fuser=request.POST['fuser']
    fpass=request.POST['fpass']
    res=faculty_login.objects.filter(fuser=fuser,fpass=fpass)
    if len(res)==1:
        #session created
        request.session['fuser']=res[0].fuser
        return redirect('home')
    else:
        return render(request,'faculty.html',{'error':'Username or Password Incorrect!!!'})
        
def home(request):
    if request.session.get('fuser'):
        return render(request,'home.html')
    else:
        return redirect('/faculty/')
        
def logout(request):
    #session deleted
    del request.session['fuser']
    return redirect('/faculty/')
    
def account(request):
    if request.session.get('fuser'):
        return render(request,'account.html')
    else:
        return redirect('/faculty/')
        
def create_account(request):
    rollno=request.POST['rollno']
    sname=request.POST['sname']   
    spass=request.POST['spass']
    
    res=students.objects.filter(rollno=rollno)
    
    if len(res):
        return render(request,'account.html',{'msg':'student already exists with this rollno'})
    else:
        q=students(rollno=rollno, sname=sname, spass=spass)
        q.save()
        return render(request,'account.html',{'msg':'Account created successfully!!!!'})

def marks(request):
    
    if request.session.get('fuser'):
        res = students.objects.all()
        return render(request,'marks.html',{'res':res})
    else:
        return redirect('/faculty/')
    
def updated_marks(request):
        marks=request.POST.getlist('nums')
        res=students.objects.all()
        ln=len(res)+1
        for i,j in zip(range(1,ln),marks):
            upd=students.objects.get(id=i)
            upd.marks=j
            upd.save()
        res=students.objects.all()
        return render(request,'updated_marks.html',{'res':res})
    
def chk_marks(request):
        res=students.objects.all()
        return render(request,'updated_marks.html',{'res':res})
       