from django.contrib import admin

from .models import Index_user, Join_table_user

# Register your models here.

admin.site.register(Index_user),
admin.site.register(Join_table_user)