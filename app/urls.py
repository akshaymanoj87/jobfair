from django.urls import path
from app import views

urlpatterns = [
   path('',views.home),
   path('employe/',views.employee_registration),
   path('employer/',views.employer_registration),


   path('admin_signup/',views.admin_signup),
   path('admin_login/',views.admin_login),
   path('logout/',views.logout),
   path('employer/',views.employer_registration),
   path('view_employee/',views.admin_view_employee),
   path('view_employer/',views.admin_view_employer),
   path('admin_index/',views.admin_index),
   
   


   

   ]