from django.shortcuts import render,redirect
from .forms import PatientCreationForm,PatientUpdationForm,HODCreationForm,UserLoginForm
from . models import Patient,HOD
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
#from django.generic.views import CreateView


def homepage(request):
    return render(request,"Feedback/homepage.html")

def dashboard(request):
    return render(request,'Feedback/dashboard.html')


def addHOD(request):
    if request.method=='POST':
        form=HODCreationForm(request.POST)
        if form.is_valid():
            hod_email=form.cleaned_data['email']
            passwd=form.cleaned_data['password']
            record=HOD(email=hod_email,password=passwd)
            record.save()
            return HttpResponseRedirect(reverse('login'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/HODSignUp.html',{'form':form,'field_error':field_error})
    else:
        form=HODCreationForm()
    return render(request,'Feedback/HODSignUp.html',{'form':form})
    
def login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            hod_email=form.cleaned_data['email']
            passwd=form.cleaned_data['password']
            in_HOD=HOD.objects.filter(email=hod_email,password=passwd)
            if in_HOD.exists():
                request.session['admin_ses']=hod_email
                return HttpResponseRedirect(reverse('dashboard'))
            
            else:
                no_account="Your account does not exists"
                return render(request,'Feedback/login.html',{'form':form,'no_account':no_account})         
        else:
            field_error="Invalid Fields"
            return render(request,'Feedback/login.html',{'form':form,'field_error':field_error})

    else:
        form=UserLoginForm()
    return render(request,'Feedback/login.html',{'form':form})




def patientfeedback(request):
    if request.method=='POST':
        form=PatientCreationForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data['patient_ID']
            request.session['user_session']=user
            record=Patient(patient_ID=user,Rating="0",area_of_issue="0",explanation="0")
            record.save()
            return HttpResponseRedirect(reverse('Feedbackform'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/feedbackstart.html',{'form':form,'field_error':field_error})
    else:
        form=PatientCreationForm()
    return render(request,'Feedback/feedbackstart.html',{'form':form})


def Feedbackform(request):
    if request.method=='POST':
        form=PatientUpdationForm(request.POST)
        if form.is_valid():
            rating=form.cleaned_data['Rating']
            Dep=form.cleaned_data['department']
            Area_of_issue=form.cleaned_data['area_of_issue']
            Explanation=form.cleaned_data['explanation']
            currentuser=request.session['user_session']
            record=Patient.objects.filter(patient_ID=currentuser).update(Rating=rating,department=Dep,area_of_issue=Area_of_issue,explanation=Explanation)
            try:
                del request.session['user_session']
            except KeyError:
                pass
            return HttpResponseRedirect(reverse('homepage'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/Feedbackform.html',{'form':form,'field_error':field_error,'currentuser':currentuser})

    else:
        form=PatientUpdationForm()
    
    return render(request,'Feedback/Feedbackform.html',{'form':form})

    


def logout(request):
    try:
        del request.session['admin_ses']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))
