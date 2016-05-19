from django.db import models

class daily_work(models.Model):
    date_time = models.DateField()
    number_plate = models.CharField(max_length=100)
    load_type = models.CharField(max_length=100)
    tonnes = models.IntegerField(default=0)
    trips = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    

    def __str__(self):

        return "%s" % self.customer_name
    
class customer(models.Model):
    date_time = models.DateField()
    customer_name = models.ForeignKey(daily_work)
    customer_id = models.IntegerField(default=0)
    amt_deposited = models.DecimalField(max_digits=8, decimal_places=2)
    balance_amt = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s" % self.date_time
    
class employee(models.Model):
    date_time = models.DateField()
    employee_name = models.CharField(max_length=100)
    amt_paid = models.DecimalField(max_digits=8, decimal_places=2)
    balance_amt = models.DecimalField(max_digits=8, decimal_places=2)
    employee_id = models.IntegerField(default=0)
    phone_contact = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.date_time
    
class repairs_maintanace(models.Model):
    date_time = models.DateField()
    mechanic_name = models.CharField(max_length=100)
    amt_paid = models.DecimalField(max_digits=8, decimal_places=2)
    balance_amt = models.DecimalField(max_digits=8, decimal_places=2)
    part_name = models.CharField(max_length=100)
    part_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s" % self.date_time
    
    

# Create your models here.
