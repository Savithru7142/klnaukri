from django.shortcuts import render, redirect
from .forms import *

def jobseekerapp(request):
    return render(request,'jobseekerapp/jobseekerhomepage.html')

def addprofile(request):
    if request.method == 'POST':
        form = JobseekerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profilelist')
    else:
        form = JobseekerProfileForm()

    return render(request,'jobseekerapp/addprofile.html', {'form': form})

def profilelist(request):
    profiles=JobSeekerProfile.objects.all()
    return render(request,'jobseekerapp/profilelist.html', {'profiles': profiles})