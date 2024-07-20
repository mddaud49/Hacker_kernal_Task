from django import forms
from .models import*
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Author.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        
        return email
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()