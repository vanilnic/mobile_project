from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import FormView
from django.db.models import Sum

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
@xframe_options_exempt
def main_view(request):
    money = User.objects.get(id=request.user.id).balance
    try:
        categories = Planing.objects.all().filter(user=request.user)[0]
    except:
        print('111')
        Planing(user=request.user).save()
    return render(request, 'android/main.html', {'categories': categories, 'money': money})

@xframe_options_exempt
@login_required
def plan_view(request):
    try:
        print(Planing.objects.all().filter(user=request.user)[0])
    except:
        Planing(user=request.user).save()
    try:
        categories = Planing.objects.all().filter(user=request.user)[0]
        plan_balance = Planing.objects.all().filter(user=request.user)[0].plan_balance
    except:
        print('хуй')
        plan_balance = 0


    if request.POST:
        if 'add_balance' in request.POST:
            print(request.POST['plan_balance'])
            print(request.user.id)
            if request.POST['plan_balance']:
                try:
                    print(Planing.objects.all().filter(user=request.user)[0])
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = request.POST['plan_balance']
                    db.budget = request.POST['plan_balance']
                    db.tochki = 0
                    db.product = 0
                    db.podar = 0
                    db.obraz = 0
                    db.dosug = 0
                    db.cafe = 0
                    db.home = 0
                    db.zdor = 0
                    db.save()
                    return redirect('planing')
                except:
                    print('пизда')
                    Planing(plan_balance=request.POST['plan_balance'], user=request.user, budget=request.POST['plan_balance']).save()



    return render(request, 'android/plan.html', {'plan_balance': plan_balance, 'categories': categories})

@login_required
@xframe_options_exempt
def plan_frame_view(request, id=None):
    bog = 'top.location.reload();'
    categoria = Categories.objects.all().filter(id=id)
    print(categoria[0].images)
    categoria = categoria[0]

    if request.POST:
        if 'save_limit' in request.POST:
            if request.POST['limit_categoria']:
                print(request.POST['limit_categoria'])
                print(Categories.objects.all().filter(id=id)[0].title)
                categ = Categories.objects.all().filter(id=id)[0].title
                if categ == 'Здоровье':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.zdor)
                    db.zdor = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Дом':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.home)
                    db.home = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Кафе':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.cafe)
                    db.cafe = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Досуг':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.dosug)
                    db.dosug = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Образование':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.obraz)
                    db.obraz = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Подарки':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.podar)
                    db.podar = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Продукты':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.product)
                    db.product = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                elif categ == 'Другое':
                    db = Planing.objects.get(user=request.user)
                    db.plan_balance = int(db.plan_balance) + int(db.tochki)
                    db.tochki = request.POST['limit_categoria']
                    print(db.plan_balance)
                    db.plan_balance = int(db.plan_balance) - int(request.POST['limit_categoria'])
                    print(db.plan_balance)
                    db.save()
                return render(request, 'android/plan_frame.html', {'bog': bog, 'categoria': categoria})


    return render(request, 'android/plan_frame.html',{'categoria': categoria})

@login_required
def report_view(request):
    return render(request, 'android/otchet.html')

@login_required
@xframe_options_exempt
def add_income_view(request, del_id=None):
    bog = 'top.location.reload();'
    if del_id is not None:
        db1 = ExpInc.objects.get(id=del_id)
        new_balance = User.objects.get(id=request.user.id)
        print(new_balance.balance)
        new_balance.balance = int(new_balance.balance) - int(db1.money)
        new_balance.save()
        print(db1.money)
        ExpInc.objects.get(id=del_id).delete()
        return render(request, 'android/add_dohod.html', {'bog': bog})

    incomes = ExpInc.objects.all().filter(user=request.user, type='I').order_by('-id')

    if request.POST:
        form = AddDohod(request.POST)
        if form.is_valid():
            db = form.save(commit=False)
            db.type = 'I'
            db.user = request.user
            db1 = User.objects.get(id=request.user.id)
            db1.balance = int(db1.balance) + int(request.POST['money'])
            db1.save()
            db.save()
            return render(request, 'android/add_dohod.html', {'incomes': incomes, 'bog': bog})

    return render(request, 'android/add_dohod.html', {'incomes': incomes})

@login_required
@xframe_options_exempt
def add_expenditure_view(request, id=None, del_id=None):
    bog = 'top.location.reload();'
    if del_id is not None:
        db1 = ExpInc.objects.get(id=del_id)
        new_balance = User.objects.get(id=request.user.id)
        print(new_balance.balance)
        new_balance.balance = int(new_balance.balance) + int(db1.money)
        new_balance.save()
        print(db1.money)

        categ = Categories.objects.all().filter(title=id)[0].title
        if categ == 'Здоровье':
            db = CategExp.objects.get(user=request.user)
            print(db.zdor)
            db.zdor = int(db.zdor) - int(db1.money)
            print(db.zdor)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Дом':
            db = CategExp.objects.get(user=request.user)
            db.home = int(db.home) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Кафе':
            db = CategExp.objects.get(user=request.user)
            db.cafe = int(db.cafe) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Досуг':
            db = CategExp.objects.get(user=request.user)
            db.dosug = int(db.dosug) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Образование':
            db = CategExp.objects.get(user=request.user)
            db.obraz = int(db.obraz) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Подарки':
            db = CategExp.objects.get(user=request.user)
            db.podar = int(db.podar) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Продукты':
            db = CategExp.objects.get(user=request.user)
            db.product = int(db.product) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})
        elif categ == 'Другое':
            db = CategExp.objects.get(user=request.user)
            db.tochki = int(db.tochki) - int(db1.money)
            db.save()
            ExpInc.objects.get(id=del_id).delete()
            return render(request, 'android/add_rashod.html', {'bog': bog})



    bog = 'top.location.reload();'
    try:
        incomes = ExpInc.objects.all().filter(user=request.user, type='E').order_by('-id')
        categories = CategExp.objects.all().filter(user=request.user)[0]
    except:
        CategExp(user=request.user).save()
        return redirect('add_expenditure')

    print(Categories.objects.all().filter(id=id))

    if request.POST:
        form = AddDohod(request.POST)
        if form.is_valid():
            db = form.save(commit=False)
            db.type = 'E'
            try:
                db.categori = Categories.objects.all().filter(id=id)[0].title
            except:
                return redirect('add_expenditure')
            print(db.categori)
            if db.categori == 'None':
                return redirect('add_expenditure')

            db.user = request.user
            db1 = User.objects.get(id=request.user.id)
            db1.balance = int(db1.balance) - int(request.POST['money'])
            db1.save()
            db.save()

            try:
                categ = Categories.objects.all().filter(id=id)[0].title

                if categ == 'Здоровье':
                    db = CategExp.objects.get(user=request.user)
                    db.zdor = int(db.zdor) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Дом':
                    db = CategExp.objects.get(user=request.user)
                    db.home = int(db.home) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Кафе':
                    db = CategExp.objects.get(user=request.user)
                    db.cafe = int(db.cafe) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Досуг':
                    db = CategExp.objects.get(user=request.user)
                    db.dosug = int(db.dosug) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Образование':
                    db = CategExp.objects.get(user=request.user)
                    db.obraz = int(db.obraz) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Подарки':
                    db = CategExp.objects.get(user=request.user)
                    db.podar = int(db.podar) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Продукты':
                    db = CategExp.objects.get(user=request.user)
                    db.product = int(db.product) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
                elif categ == 'Другое':
                    db = CategExp.objects.get(user=request.user)
                    db.tochki = int(db.tochki) + int(request.POST['money'])
                    db.save()
                    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes, 'bog': bog})
            except:
                redirect('add_expenditure')
        else:
            print('dffgdfdgfgd')

    return render(request, 'android/add_rashod.html', {'categories': categories, 'incomes': incomes})


@login_required
@xframe_options_exempt
def report_income_view(request):
    incomes = ExpInc.objects.all().filter(user=request.user, type='I')
    sum = ExpInc.objects.all().filter(user=request.user, type='I').aggregate(Sum('money'))['money__sum']

    return render(request, 'android/otch_dohod.html', {'incomes': incomes, 'sum': sum})

@login_required
@xframe_options_exempt
def report_expenditure_view(request):
    sum = ExpInc.objects.all().filter(user=request.user, type='E').aggregate(Sum('money'))['money__sum']

    categories = CategExp.objects.all().filter(user=request.user)[0]
    plan = Planing.objects.all().filter(user=request.user)[0]
    db = CategExp.objects.all().filter(user=request.user)[0]
    db.zdor = int(plan.zdor) - int(db.zdor)
    db.home = int(plan.home) - int(db.home)
    db.cafe = int(plan.cafe) - int(db.cafe)
    db.dosug = int(plan.dosug) - int(db.dosug)
    db.obraz = int(plan.obraz) - int(db.obraz)
    db.podar = int(plan.podar) - int(db.podar)
    db.product = int(plan.product) - int(db.product)
    db.tochki = int(plan.tochki) - int(db.tochki)

    return render(request, 'android/otch_rashod.html', {'categories': categories, 'db': db, 'sum': sum})