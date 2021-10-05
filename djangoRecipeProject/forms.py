from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length= 100)
    lastname = forms.CharField(max_length= 100)
    email = forms.EmailField()
    message = forms.CharField(widget= forms.Textarea)


class SubscriberForm(forms.Form):
    subscription = forms.EmailField()