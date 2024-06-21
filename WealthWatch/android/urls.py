from django.urls import path
from .views import *


urlpatterns = [
    path('', greeting_view, name='greeting'),
    path('registration/', RegisterView.as_view(), name="registration"),

    path('main/', main_view, name='main'),
    path('planing/', plan_view, name='planing'),
    path('report/', report_view, name='report'),
    path('add_income/', add_income_view, name='add_income'),
    path('add_expenditure/', add_expenditure_view, name='add_expenditure'),
    path('report_income/', report_income_view, name='report_income'),
    path('report_expenditure/', report_expenditure_view, name='report_expenditure'),

]