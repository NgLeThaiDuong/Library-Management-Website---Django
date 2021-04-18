from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.forms import modelform_factory
from django.http import HttpResponse
import datetime
from datetime import timedelta
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from django.middleware.csrf import rotate_token
from django.contrib.auth.models import Group

from libmagapp.models import Book
from libmagapp.models import BookLending
from libmagapp.models import BookRequest
from libmagapp.models import Member
from libmagapp.models import LibraryCard
from libmagapp.models import Librarian
from libmagapp.models import BookLendingForm
from libmagapp.models import BookReturnForm
# Create your views here.

def index (request):
    return render(request, "index.html")
    
@login_required
def add_book (request):
    if not request.user.is_staff:
        return redirect('login')
    form = modelform_factory(Book,exclude=['status'])
    if request.method == 'POST':
        result = form(request.POST,request.FILES)
        if result.is_valid():
            result.save()
        return render(request,"add_book.html", {'form':form})
    else:
        return render(request,"add_book.html", {'form':form})
@login_required
def add_member(request):
    if not request.user.is_staff:
        return redirect('login')
    form = modelform_factory(Member,fields="__all__",widgets={'date_of_birth':forms.DateInput(attrs={'class':'datepicker'},)})
    if request.method == 'POST':
        result = form(request.POST, request.FILES)
        if result.is_valid():
            result.save()
        return render(request,"add_member.html", {'form':form})
    else:
        return render(request,"add_member.html", {'form':form})


@login_required
def add_lending (request):
    if not request.user.is_staff:
        return redirect('login')
    form = modelform_factory(BookLending, form=BookLendingForm, fields=['member', 'book'])
    if request.method == 'POST':
        lending = form(request.POST)
        print(request.POST)
        if lending.is_valid():
            book = Book.objects.get(id=request.POST['book'])
            book.status = False
            book.save()
            lending.save()
        return render(request,"add_lending.html", {'form':form})
    else:
        return render(request,"add_lending.html", {'form':form})

@login_required
def return_book(request):
    if not request.user.is_staff:
        return redirect('login')
    form = modelform_factory(BookLending, form=BookReturnForm, fields=['book'])
    if request.method == 'POST':
        return_book = form(request.POST)
        if return_book.is_valid():
            lending = BookLending.objects.get(book = request.POST['book'], return_date=None)
            lending.return_date = datetime.date.today()
            lending.save()
            book = Book.objects.get(id = request.POST['book'])
            book.status = True
            book.save()
        return render(request, 'add_return.html', {'form':form})
    else:
        return render(request, 'add_return.html', {'form':form})

@login_required
def add_request (request):
    mem = Member.objects.get(email=request.user.username)
    form = modelform_factory(BookRequest, exclude=['status', 'member'])
    if request.method == 'POST':
        req = BookRequest(member = mem, 
                        requested_book_title=request.POST['requested_book_title'],
                        requested_book_author=request.POST['requested_book_author'])
        req.save()
        return render(request,"add_request.html", {'form':form})
    else:
        return render(request,"add_request.html", {'form':form})

@login_required
def add_librarian (request):
    if not request.user.is_superuser:
        return redirect('login')
    form = modelform_factory(Librarian, fields="__all__")
    if request.method == 'POST':
        librarian = form(request.POST)
        if librarian.is_valid():
            librarian.save()
        return render(request,"add_librarian.html", {'form':form})
    else:
        return render(request,"add_librarian.html", {'form':form})

@login_required
def add_card (request):
    if not request.user.is_staff:
        return redirect('login')
    form = modelform_factory(LibraryCard, exclude=['deactive_date'])
    if request.method == 'POST':
        card = form(request.POST)
        if card.is_valid():
            card.save()
        return render(request,"add_card.html", {'form':form})
    else:
        return render(request,"add_card.html", {'form':form})

def home (request):
    book_list = Book.objects.all()
    status =[]
    for book in book_list:
        lending_list = BookLending.objects.filter(book__id=book.id)
        print(book.book_cover.url)
        flag = 0
        for l in lending_list:
            if l.return_date is None:
                flag = 1
                continue
        if flag: status.append('lending')
        else: status.append('available')
    book_list = list(zip(book_list, status))
    return render(request, 'home.html', {'book_list': book_list, 'status':status})

def compact_view(request):
    book_list = Book.objects.all()
    status =[]
    for book in book_list:
        lending_list = BookLending.objects.filter(book__id=book.id)
        print(book.book_cover.url)
        flag = 0
        for l in lending_list:
            if l.return_date is None:
                flag = 1
                continue
        if flag: status.append('lending')
        else: status.append('available')
    book_list = list(zip(book_list, status))
    return render(request, 'compact_view.html', {'book_list': book_list, 'status':status})



@login_required
def member (request):
    if not request.user.is_staff:
        return redirect('login')
    member_list = Member.objects.all()
    return render(request, 'member.html', {'member_list': member_list})




@login_required
def lending (request):
    if not request.user.is_staff:
        return redirect('login')
    lending_list = BookLending.objects.all()
    member = []
    book = []
    due_date = []
    for lending in lending_list:
        mbr = Member.objects.get(pk=lending.member.id)
        member.append(mbr)
        bok = Book.objects.get(pk=lending.book.id)
        book.append(bok)
        due = lending.creation_date
        due_date.append(due)

    lending_list = zip(lending_list, member, book)
    return render(request, 'lending.html', {'lending_list':lending_list})


@login_required
def mem_infor(request, mem_id):
    if not request.user.is_staff:
        user_id = Member.objects.get(email=request.user.username)
        if mem_id != user_id.pk:
            return redirect(reverse('login'))
    member = Member.objects.get(pk=mem_id)
    loan_times = BookLending.objects.filter(member__id=member.id)
    # num_loaned_books = loan_times.values('book').distinct().count()
    num_loaned_times = loan_times.count()
    num_not_return = loan_times.filter(return_date=None).count()

    returned_book = {}
    not_return_book = {}
    for time in loan_times:
        if time.return_date is None:
            not_return_book[Book.objects.get(pk=time.book.id)]=time
        else:
            returned_book[Book.objects.get(pk=time.book.id)]=time

    return render(request, 'member_infor.html',{'member': member,
                                                'num_loaned_times':num_loaned_times,
                                                'num_not_return':num_not_return,
                                                'returned_books':returned_book,
                                                'not_return_books':not_return_book})

@login_required
def delete_book(request, id):
    if not request.user.is_staff:
        return redirect('login')
    context ={}
    obj = get_object_or_404(Book, id = id) 
    if request.method =="POST": 
        obj.delete() 
        return redirect(reverse('home'))
  
    return render(request, "delete_book.html", context) 


@login_required
def delete_member(request, id):
    if not request.user.is_staff:
        return redirect('login')
    context ={}
    # request.META["CSRF_COOKIE"] = _get_new_csrf_key()
    obj = get_object_or_404(Member, id = id)   
    if request.method =="POST": 
        obj.delete() 
        return redirect(reverse('member'))

    return render(request, "delete_member.html", context) 

def update_member(request, mem_id):
    if request.method == "GET":
        try:
            member = Member.objects.get(pk=mem_id)
            return render(request,"update_member.html", {'form':form})
    
        except:
            return HttpResponse("Trang khong ton tai ")

    form = modelform_factory(Member,fields="__all__",)
    if request.method == 'POST':
        member = form(request.POST)
        if member.is_valid():
            member.save()
        return mem_infor(request, mem_id)
