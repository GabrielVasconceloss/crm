from django.contrib import admin
from .models import Camp, status, Customer, Contact, Opportunity, Activity

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


admin.site.register(Camp)
admin.site.register(status)
admin.site.register(Contact)
admin.site.register(Opportunity)
admin.site.register(Activity)