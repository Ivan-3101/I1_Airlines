from django.contrib import admin

from .models import Flight, Airport
# .models = . for current working directory and models is the file name

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)