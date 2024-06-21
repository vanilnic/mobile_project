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
    path('plan_form/<id>/', plan_frame_view, name='plan_form'),
    # path('rashod_form/<id>/', rashod_frame_view, name='rashod_form'),
    path('add_expenditure/<id>/', add_expenditure_view, name='add_expenditur'),
    path('add_expenditure/<id>/<del_id>/', add_expenditure_view, name='del_expenditure'),
    path('add_income/<del_id>/', add_income_view, name='del_income'),
]