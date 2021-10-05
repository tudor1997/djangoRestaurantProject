from django.shortcuts import render
from .models import Burgers, Desserts, Drinks, Pizzas,Toasts , Messages, Subscribers
from djangoRecipeProject.forms import ContactForm, SubscriberForm
# Create your views here.
def index(request):
     subForm = SubscriberForm(request.POST)
     if subForm.is_valid():
          subscriptions = request.POST.get('subscription')
          subscribe = Subscribers(email = subscriptions)
          subscribe.save()
     return render(request, 'index.html')

     
def menu(request):
     burgers = Burgers.objects.all()
     pizzas = Pizzas.objects.all()
     toasts = Toasts.objects.all()
     desserts = Desserts.objects.all()
     drinks = Drinks.objects.all()

     subForm = SubscriberForm(request.POST)
     if subForm.is_valid():
          subscriptions = request.POST.get('subscription')
          subscribe = Subscribers(email = subscriptions)
          subscribe.save()
     return render(request, 'menu.html', {'burgers':burgers, 'pizzas':pizzas, 'toasts':toasts, 
     'desserts':desserts,'drinks':drinks })


def contact(request):
          form = ContactForm(request.POST)
          if form.is_valid():
               firstname = request.POST.get('firstname')
               lastname = request.POST.get('lastname')
               email = request.POST.get('email')
               message = request.POST.get('message')
               instance = Messages(firstname = firstname, lastname = lastname, email = email, message = message)
               instance.save()

          subForm = SubscriberForm(request.POST)
          if subForm.is_valid():
               subscriptions = request.POST.get('subscription')
               subscribe = Subscribers(email = subscriptions)
               subscribe.save()
          return render(request, 'contact.html', {'form': form})

def about(request):
          subForm = SubscriberForm(request.POST)
          if subForm.is_valid():
               subscriptions = request.POST.get('subscription')
               subscribe = Subscribers(email = subscriptions)
               subscribe.save()
          return render(request, 'about.html')