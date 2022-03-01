from django.contrib import admin

from .models import Vacancy,Contact,Feedback

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Contact)
admin.site.register(Feedback)