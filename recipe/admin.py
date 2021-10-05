from django.contrib import admin
from .models import Burgers,Pizzas,Toasts,Desserts,Drinks,Messages,Subscribers
# Register your models here.
admin.site.register(Burgers)
admin.site.register(Pizzas)
admin.site.register(Toasts)
admin.site.register(Desserts)
admin.site.register(Drinks)
admin.site.register(Messages)
admin.site.register(Subscribers)