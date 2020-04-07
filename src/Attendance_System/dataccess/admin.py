from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('id', 'first_name', 'last_name','password') # add this
    # list_display = ('id',) # add this

# Register your models here.
# admin.site.register(User, TodoAdmin) # add this