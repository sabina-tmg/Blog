# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    message = forms.CharField(widget=forms.Textarea)

# from django import forms

# class CommentForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     body = forms.CharField(widget=forms.Textarea)
