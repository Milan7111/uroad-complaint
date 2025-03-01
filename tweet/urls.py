from django.urls import path
from . import views
from .views import register_view, login_view, logout_view, index, submit_complaint, ComplaintListCreateView, complaint_form, complaints_list
from .views import dashboard

app_name = 'tweet'

urlpatterns = [
    path('', views.index, name='home'),
    path("submit-complaint/", submit_complaint, name="submit_complaint"),
    path('add-complaint/', complaint_form, name='complaint_form'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('complaints/', complaints_list, name='complaints'),
    path("complaints-list/", complaints_list, name="complaints_list"),
    path("dashboard/", dashboard, name="dashboard"),
    
]
