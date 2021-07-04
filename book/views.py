from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
# Create your views here.
from .models import *

def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'book/home.html', context)

def bookList(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/booklist.html', context)

def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'book/bookCreate.html', context)


def updateBook(request, pk):
    books = Book.objects.get(id=pk)
    form = BookForm(instance=books)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('books')

    context = {'form': form}
    return render(request, 'book/bookCreate.html', context)

def deleteBook(request, pk):
    books = Book.objects.get(id=pk)
    if request.method == 'POST':
        books.delete()
        return redirect('books')
    context = {'item': books}
    return render(request, 'book/delete.html', context)

def userList(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'book/userList.html', context)

def createUser(request):
    form = UserForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_List')
        else:
            print(form.errors)
    context = {'form': form, }
    return render(request, 'book/userCreate.html', context )


def updateUser(request, pk):
    users = User.objects.get(id=pk)
    form = UserForm(instance=users)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('user_List')

    context = {'form': form}
    return render(request, 'book/userCreate.html', context)


def deleteUser(request, pk):
    users = User.objects.get(id=pk)
    if request.method == 'POST':
        users.delete()
        return redirect('user_List')
    context = {'item': users}
    return render(request, 'book/deleteUser.html', context)


def rentList(request):
    rents = Rent.objects.all()
    context = {'rents': rents}
    return render(request, 'book/rentList.html', context)


def createRent(request):
    form = RentForm()
    if request.method == 'POST':

        user_id = request.POST["user"]
        rents = Rent.objects.filter(user_id=user_id)
        totalRent = rents.count()

        bookId = request.POST["book"]
        books = Rent.objects.filter(book_id=bookId)
        totalBook = books.count()

        bookCopy = Book.objects.get(id=bookId).numberOfBook

        form = RentForm(request.POST)
        if form.is_valid():

            if totalRent <2 and totalBook < bookCopy:
                form.save()
            return redirect('rent_List')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'book/rentCreate.html', context)



def updateRent(request, pk):
    rents = Rent.objects.get(id=pk)
    form = RentForm(instance=rents)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=rents)
        if form.is_valid():
            form.save()
            return redirect('rent_List')

    context = {'form': form}
    return render(request, 'book/rentCreate.html', context)