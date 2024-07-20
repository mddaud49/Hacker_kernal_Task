from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.paginator import Paginator
import xlwt
from django.http import HttpResponse
from .serializers import *
from io import BytesIO
import pandas as pd


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView

class AddAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = reverse_lazy('author_list')

    def form_valid(self, form):
        messages.success(self.request, 'Author added successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add author. Please correct the errors.')
        return super().form_invalid(form)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')  
            return redirect('book_list') 
        else:
            messages.error(request, 'Failed to add book. Please correct the errors.')  
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def add_borrow_record(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Borrow record added successfully.')  # Success message
            return redirect('borrow_record_list')  # Redirect to the list of borrow records or any other page
        else:
            messages.error(request, 'Failed to add borrow record. Please correct the errors.')  # Error message
    else:
        form = BorrowRecordForm()
    return render(request, 'add_borrow_record.html', {'form': form})


class AuthorListView(ListView):
    model = Author
    paginate_by = 10
    template_name = 'author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    Context={
        'page_obj': page_obj,
        'data':books
    }
    return render(request, 'book_list.html',Context)

def borrow_record_list(request):
    borrow_records = BorrowRecord.objects.all()
    paginator = Paginator(borrow_records, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    Context={
        'page_obj': page_obj,
        'data':borrow_records
    }
    return render(request, 'borrow_record_list.html',Context)

def author_to_excel(request):
    author = Author.objects.all()
    serializer = Authorserializer(author, many=True) 
    df = pd.DataFrame(serializer.data)  
    author_file = BytesIO()  
    df.to_excel(author_file, index=False, engine='openpyxl')  
    author_file.seek(0) 
    response = HttpResponse(author_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=author.xlsx'
    return response


def book_to_excel(request):
    book = Book.objects.all()
    serializer = Bookserializer(book, many=True)
    print(serializer) 
    df = pd.DataFrame(serializer.data)  
    book_excel = BytesIO()  
    df.to_excel(book_excel, index=False, engine='openpyxl')  
    book_excel.seek(0) 
    response = HttpResponse(book_excel, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=book.xlsx'
    return response

def borrowrecord_to_excel(request):
    borrow = BorrowRecord.objects.all()
    serializer = BorrowRecordserializer(borrow, many=True)
    print(serializer) 
    df = pd.DataFrame(serializer.data)  
    borrow_excel = BytesIO()  
    df.to_excel(borrow_excel, index=False, engine='openpyxl')  
    borrow_excel.seek(0) 
    response = HttpResponse(borrow_excel, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=borrow.xlsx'
    return response
