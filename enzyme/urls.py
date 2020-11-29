from django.urls import path
from .import views

app_name='enzyme'

urlpatterns=[
    # home view
    path('home',views.enzyme_office_home,name='enzyme_offic_home'),
    path('dashboard', views.enzyme_office_dashboard, name='enzyme_offic_dashboard'),


    # list view
    path('list', views.enzyme_office_list, name='enzyme_offic_list'),

    # Detail view
    path('listdetail/<int:id>', views.enzyme_office_listdetail, name='enzyme_offic_listdetail'),

    # Add view
    path('Add/<int:id>', views.enzyme_office_Add, name='enzyme_offic_Add'),
    path('Add/loadcomment', views.enzyme_office_loadcomment, name='enzyme_offic_loadcomment'),

    path('savecomment', views.savecomment, name='enzyme_offic_savecomment'),


    #Edit view
    path('edit/<int:id>', views.enzyme_office_edit, name='enzyme_offic_edit'),

    # Delete view
    path('delete/<int:id>', views.enzyme_office_delete, name='enzyme_offic_delete'),

    # Alternative view
    path('alternative', views.enzyme_office_alternative, name='enzyme_offic_alternative'),
    # Search result view
    path('searchresult', views.enzyme_office_searchresult, name='enzyme_offic_searchresult'),



    


]
