from django.shortcuts import render, redirect
import requests
from django.contrib.auth.hashers import make_password, check_password

from .forms import *
import pytz
import datetime

def adminapphomepage(request):
    return render(request,'adminapp/projecthomepage.html')

def printer(request):
    user_input=""
    if request.method == 'POST':
        user_input = request.POST['klu']
    a1= {'klu':user_input}
    return render(request,'adminapp/printer.html', a1)

def timetable(request):
    return render(request,'adminapp/timetable.html')

def time1(request):
    a2=""
    if request.method == 'POST':
        klu = request.POST.get('klu')
        tz = pytz.timezone(klu)
        current_time = datetime.datetime.now(tz)
        a2 = f"Current Time is: {current_time}"
    return render(request,'adminapp/time1.html', {'a2':a2})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password= make_password(form.cleaned_data['password'])
            user.save()

            return redirect('adminapphomepage')
    else:
        form = UserForm()

    return render(request, 'adminapp/signup.html', {'form': form})

def weather1(request):
    weather_data = {}
    error_message = ""
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "51e4f0490cfcbd5acc19e32c4fbe0f70"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if "main" in response:
            weather_data = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"],
                "humidity": response["main"]["humidity"]
            }
        else:
            error_message = "Wrong Input / No City Found"
    return render(request, "adminapp/weather.html", {
        "weather": weather_data,
        "error": error_message
    })

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user=Useraccount.objects.get(email=email)
            if check_password(password, user.password):
                print(password)
                request.session['user_email'] = user.email
                request.session['user_name']=user.firstname
                return redirect('adminapphomepage')
            else:
                error="Invalid Password"
        except Useraccount.DoesNotExist:
            error="User not found"
        return render(request, "adminapp/login.html", {"error": error})
    return render(request, "adminapp/login.html")
def logout(request):
    request.session.flush()
    return redirect('login')

