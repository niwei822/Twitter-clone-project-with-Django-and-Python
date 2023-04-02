from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Register your models here.
admin.site.unregister(Group)

#mix profile into user
class ProfileInline(admin.StackedInline):
    model = Profile

#extend User model

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

#unregister and rigister initial user
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

