from django.contrib import admin

from .models import Chore, Comment, Supply

# Register your models here.
admin.site.register(Chore)
admin.site.register(Comment)
admin.site.register(Supply)