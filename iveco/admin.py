from django.contrib import admin

from .models import daily_work
from .models import customer
from .models import employee
from .models import repairs_maintanace


    
class customerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date_time']}),
        ('Customer details', {'fields': ['customer_name']}),
        (None,               {'fields': ['customer_id']}),
        (None,               {'fields': ['amt_deposited']}),
        (None,               {'fields': ['balance_amt']}),
    ]
    list_display =  ('date_time','customer_name','customer_id','amt_deposited','balance_amt')

    list_filter = ['date_time']

class daily_workAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date_time']}),
        ('Truck details', {'fields': ['number_plate']}),
        (None,               {'fields': ['load_type']}),
        (None,               {'fields': ['tonnes']}),
        (None,               {'fields': ['trips']}),
        (None,               {'fields': ['customer_name']}),
    ]
    list_display =  ('date_time','number_plate','load_type','tonnes','trips','customer_name' )

    list_filter = ['date_time']
    #search_fields = ['play_station']

class repairs_maintanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date_time']}),
        ('Repair/Maintance details', {'fields': ['mechanic_name']}),
        (None,               {'fields': ['amt_paid']}),
        (None,               {'fields': ['balance_amt']}),
        (None,               {'fields': ['part_name']}),
        (None,               {'fields': ['part_price']}),
    ]
    list_display =  ('date_time','mechanic_name','amt_paid','balance_amt','part_name','part_price' )

    list_filter = ['date_time']



admin.site.register(repairs_maintanace, repairs_maintanceAdmin)    
admin.site.register(daily_work, daily_workAdmin)
admin.site.register(customer, customerAdmin)

# Register your models here.
