from django.urls import path
from .import views

app_name='users'

urlpatterns=[

    path('register', views.register, name='enzyme_offic_register'),
    path('profile/<str:username>', views.profile, name='enzyme_offic_profile'),
    # home for login view
    path('loginpage', views.enzyme_office_login, name='enzyme_offic_loginpage'),
    path('logout', views.logout, name='enzyme_offic_logout'),
    path('changerole', views.changerole, name='enzyme_offic_change'),

]