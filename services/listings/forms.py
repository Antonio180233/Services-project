from django.forms import ModelForm
from .models import Listing, Comment
from django import forms

class ListingForm(ModelForm):
    class Meta:
        model=Listing
        fields = ['title', 'category', 'description', 'price', 'address', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6',
                    ]
    
        
    
class UpdateForm(ModelForm):
    class Meta:
        model=Listing
        fields = ['title', 'category', 'description', 'price', 'address', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body',]
