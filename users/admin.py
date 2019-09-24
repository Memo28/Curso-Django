from django.contrib import admin

from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Configuration of the dashboard for user
    #Data to display in the table
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    #Editable data in the table
    list_editable = ('phone_number','website')
    #Enable search in the table by some specific fields
    search_fields = ('user__email','user__first_name','user__last_name','phone_number')
    #Filters
    list_filter = ('created','modified', 'user__is_active','user__is_staff')

