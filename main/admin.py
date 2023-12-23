from django.contrib import admin
from .models import *
from .models import VolunteerApplication
from .models import Donation
# Register your models here.


admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(Order)

@admin.register(VolunteerApplication)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'reasons_for_volunteering', 'skills')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'credit_card_number')