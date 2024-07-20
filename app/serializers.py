from rest_framework import serializers
from .models import Author, Book, BorrowRecord

class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class BorrowRecordserializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowRecord
        fields="__all__"