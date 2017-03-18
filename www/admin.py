from django.contrib import admin
from .models import Runner, Category, Competition, Time, Metas
# Register your models here.
admin.site.register(Runner)
admin.site.register(Category)
admin.site.register(Competition)
admin.site.register(Time)
admin.site.register(Metas)
