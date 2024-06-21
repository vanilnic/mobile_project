from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import FormView


# Create your views here.

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("main")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def greeting_view(request):
    return render(request, 'android/index.html')

@login_required
def main_view(request):
    return render(request, 'android/main.html')

@login_required
def plan_view(request):
    if request.method == 'POST':
        if 'zdorovie' in request.POST:
            print('здоровье')

        elif 'home' in request.POST:
            print('дом')
        elif 'cafe' in request.POST:
            print('кафе')
        elif 'dosug' in request.POST:
            print('досуг')
        elif 'obraz' in request.POST:
            print('образование')
        elif 'podar' in request.POST:
            print('подарок')
        elif 'product' in request.POST:
            print('продукты')
        elif 'tochki' in request.POST:
            print('другое')
    return render(request, 'android/plan.html')

@login_required
def report_view(request):
    return render(request, 'android/otchet.html')

@login_required
@xframe_options_exempt
def add_income_view(request):
    return render(request, 'android/add_dohod.html')

@login_required
@xframe_options_exempt
def add_expenditure_view(request):
    return render(request, 'android/add_rashod.html')

@login_required
@xframe_options_exempt
def report_income_view(request):
    return render(request, 'android/otch_dohod.html')

@login_required
@xframe_options_exempt
def report_expenditure_view(request):
    return render(request, 'android/otch_rashod.html')