from django.urls import path
from . import views
urlpatterns = [
    path('jobseekerhomepage/',views.jobseekerapp,name='jobseekerapp'),
    path('addprofile/', views.addprofile, name='addprofile'),
    path('profilelist/',views.profilelist,name='profilelist'),
]