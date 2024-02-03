from django.urls import path
from .views import timesheet_list, add_timesheet_entry, register_view

urlpatterns = [
    path('timesheet/', timesheet_list, name='timesheet_list'),
    path('timesheet/add/', add_timesheet_entry, name='add_timesheet_entry'),
    path('register/', register_view, name='register'),
    path('accounts/profile/', timesheet_list, name='profile_view'),
]
