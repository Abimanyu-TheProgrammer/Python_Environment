from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import DpayTopUpTransaction, Service, Testimony, Status,LaundryList,Item
from .forms import *
from datetime import datetime
from django.core.paginator import  Paginator
from django.db import connection,  IntegrityError, transaction
from collections import namedtuple
from django.forms import formset_factory
from django.contrib import messages

# Create your views here.
def registerStaff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        print(request.POST)
    else:
        form = StaffForm()
    return render(request, 'startpage/registerUser.html', {'form':form})

def registerCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        print(request.POST)
    else:
        form = CustomerForm()
    return render(request, 'startpage/registerUser.html', {'form':form})

def registerCourier(request):
    if request.method == "POST":
        form = CourierForm(request.POST)
        print(request.POST)
    else:
        form = CourierForm()
    return render(request, 'startpage/registerUser.html', {'form':form})

def login(request):
    login_form = loginForm(request.POST)
    if request.method == "POST" and login_form.is_valid():
        email = login_form.cleaned_data['email']
        raw_password = login_form.cleaned_data['password']
    
        with connection.cursor() as cursor:
            cursor.execute('SELECT password FROM SILAU.USER WHERE email = %(email)s', {'email': email})
            existing_user_password = cursor.fetchone()
            if (existing_user_password is not None) and (existing_user_password == raw_password) :
                cursor.execute('SELECT email FROM Customer WHERE email = %(email)s', {'email': email})
                customer_user = cursor.fetchone()
                if customer_user is not None:
                    request.session['user'] = 'customer'

                cursor.execute('SELECT email FROM STAFF WHERE email = %(email)s', {'email': email})
                staff_user = cursor.fetchone()
                if staff_user is not None:
                    request.session['user'] = 'staff'

                cursor.execute('SELECT email FROM COURIER WHERE email = %(email)s', {'email': email})
                courier_user = cursor.fetchone()
                if courier_user is not None:
                    request.session['user'] = 'courier'

                request.session['email'] = email	
                return redirect('startpage:home')
            else:
                messages.error(request, f'Invalid Password')
                return redirect('login')
                pass
    return render(request, 'startpage/login.html', {"login_form": loginForm()})

def logout(request):
	request.session.flush()
	return redirect('startpage:home')

def home(request):
    try:
        print(request.session['user'])
        print(request.session['email'])
        message = "You are logged in as a " + request.session['user']
    except:
        print('You Are Logged Out')
        message = 'You Are Logged Out'

    context = {'message' : message}
    return render(request, 'startpage/home.html', context)

def topUp(request):
    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM DPAY_TOPUP_TRANSACTION")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns,row)) for row in cursor.fetchall()]
        context = {'data' : data}
    return render(request, 'topUp/topupRead.html', context)

def topUpForm(request):
    if request.method == "POST":
        form = TopUp_Input(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('startpage:topup')
    form = TopUp_Input()
    return render(request, 'topUp/topUpForm.html', {'form':form})

def deleteTopup(request, email, date):
    object = DpayTopUpTransaction.objects.get(email=email, date=date)
    object.delete()
    return render(request, 'topUp/topupRead.html')

def updateTopup(request, email, date):
    object = DpayTopUpTransaction.objects.get(email=email, date=date)
    response = {'object' : object}
    form = TopUp_Update(request.POST, instance=object)
    if (form.is_valid()):
            form.save()
            return redirect('startpage:topup')
    form = TopUp_Update()
    return render(request, 'topUp/topUpUpdate.html', {'form':form, 'object':object})

def testimonyForm(request):
    if request.method == "POST":
        print(request.POST)
        # form = TestimonyForm(request.POST)
        # if (form.is_valid()):
        #     form.save()
    form = TestimonyForm()
    return render(request, 'testimony/testimonyForm.html', {'form':form})

def deleteTestimony(request, email, date):
    object = Testimony.objects.get(email=email, transaction_date=date)
    object.delete()
    return render(request, 'testimony/testimonyRead.html')

def updateTestimony(request, email, date):
    # object = Testimony.objects.get(email=email, transaction_date=date)
    # response = {'object' : object}
    # form = Testimony_Update(request.POST, instance=object)
    # if (form.is_valid()):
    #         form.save()
    #         return redirect('startpage:testimony')
    if request.method == 'POST':
        print(request.POST)
        # form = Testimony_Update(request.POST)
        # if (form.is_valid()):
        #     # form.save()
        #     try:
        #         with connection.cursor() as cursor:
        #             with transaction.atomic():
        #                 cursor.execute("""\
        #                 UPDATE TESTIMONY SET status = %s, rating = %s
        #                 WHERE email=%s AND transaction=%s""", [request.])
        #     except IntegrityError:
        #         pass
        return redirect('startpage:testimony')
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT email, transaction_date FROM TESTIMONY where email=%s AND transaction_date=%s LIMIT 1;", [email, date] )
            data = cursor.fetchone()
            if data is None:
                return redirect('apotek/')
            columns = [col[0] for col in cursor.description]
            old_data = dict(zip(columns, data))
            form = Testimony_Update(initial = old_data)
        return render(request, 'testimony/testimonyUpdate.html', {'form':form, 'old_data': old_data})

def readTestimony(request):
    # testimony_data = Testimony.objects.all()
    
    # paginator = Paginator(testimony_data, 3)
    # page = request.GET.get('page')
    # testimony_data = paginator.get_page(page)

    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM TESTIMONY")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns,row)) for row in cursor.fetchall()]
        context = {'data' : data}
    # response = {'testimony_data' : testimony_data}
    return render(request, 'testimony/testimonyRead.html', context)



def readService(request):
    # service_data = Service.objects.all()

    # paginator = Paginator(service_data, 3)
    # page = request.GET.get('page')
    # service_data = paginator.get_page(page)

    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM SERVICE")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns,row)) for row in cursor.fetchall()]
        context = {'data' : data}

    # response = {'service_data' : service_data}
    return render(request, 'service/serviceRead.html', context)

def updateService(request, code):
    # object = Service.objects.get(code = code)
    # response = {'object' : object}
    # form = Service_Update(request.POST, instance=object)
    # if (form.is_valid()):
    #         form.save()
    #         return redirect('startpage:service')
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            try:
                with connection.cursor() as cursor:
                    with transaction.atomic():
                        cursor.execute("""\
                        UPDATE Service SET name = %s, duration = %s, price = %s 
                        WHERE code=%s""",
                                    [cleaned.get("name"), cleaned.get("duration"),
                                    cleaned.get('price'), cleaned.get('code')])
            except IntegrityError:
                pass
            return redirect('startpage:service')
    else:
        form = ServiceForm(initial={'code':code})
    return render(request, 'service/serviceUpdate.html', {'form':form})

def statusRead(request):
    # status_data = Status.objects.all()
    # response = {'status_data' : status_data}
    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM STATUS")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns,row)) for row in cursor.fetchall()]
        context = {'data' : data}
    return render(request, 'status/status.html', context)


def updateLaundryList(request, email, date):
    object = LaundryList.objects.get(email = email,date=date)
    response = {'object' : object}
    form = LaundryList_Update(request.POST, instance=object)
    if (form.is_valid()):
            form.save()
            return redirect('startpage:laundryList')
    form = LaundryList_Update()
    return render(request, 'laundryList/laundryListUpdate.html', {'form':form, 'object':object})

def deleteLaundryList(request, email, date):
    object = LaundryList.objects.get(email = email,date=date)
    object.delete()
    return render(request, 'laundryList/laundryListRead.html')

def readLaundryList(request):
    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM LAUNDRY_LIST")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns,row)) for row in cursor.fetchall()]
        context = {'data' : data}
    return render(request, 'laundryList/laundryListRead.html', context)

def laundryListForm(request):
    if request.method == "POST":
        form = LaundryListForm(request.POST)
        if (form.is_valid()):
            form.save()
    form = LaundryListForm()
    return render(request, 'laundryList/laundryListForm.html', {'form':form})

def readItem(request):
    # Item_data = Item.objects.all()
    # response = {'Item_data' : Item_data}
    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM ITEM")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns,row)) for row in cursor.fetchall()]
        context = {'data' : data}
        if (request.user.is_authenticated):
            if (request.session['user']=='staff'):
                return render(request, 'item/itemRead.html', context)
    return render(request, 'item/itemRead2.html', context)

def itemForm(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('startpage:item')
    form = ItemForm()
    return render(request, 'item/itemForm.html', {'form':form})