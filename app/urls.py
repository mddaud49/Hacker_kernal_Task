from django.urls import path
from . import views
from .views import AddAuthorView,AuthorListView

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('add_borrow_record/', views.add_borrow_record, name='add_borrow_record'),
    path('books/', views.book_list, name='book_list'),
    path('borrow_records/', views.borrow_record_list, name='borrow_record_list'),
    path('author_to_excel/',views.author_to_excel, name='author_to_excel'),
    path('book_to_excel/',views.book_to_excel, name='book_to_excel'),
    path('borrowrecord_to_excel/',views.borrowrecord_to_excel, name='borrowrecord_to_excel'),
    path('', AddAuthorView.as_view(), name='add_author'),    
    path('author_list/', AuthorListView.as_view(), name='author_list'),
]