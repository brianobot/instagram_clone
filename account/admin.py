from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm 

# to be used within the UserAdmin admin page
class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    
# register out own model admin, based pn the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # model = models.User
    list_display = ('email','first_name', 'last_name', 'is_staff', 'is_active', 'followers')
    list_filter =  ('email','first_name', 'last_name', 'is_staff', 'is_active', )
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = [ProfileInline]
