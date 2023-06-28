from django.db import models

# Create your models here.
class Years(models.Model):
    year = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return str(self.year.year)
    
class Common_Expenses(models.Model):
    common_expenses_dues = models.IntegerField()
    number_of_units = models.IntegerField()
    revenues = models.IntegerField()
    minus_delinquent_payments = models.IntegerField()
    gross_profit = models.IntegerField()
    years = models.ForeignKey(Years, on_delete= models.CASCADE)

class Replacement_Reserves(models.Model):
    Reverves_Name = models.CharField(max_length=100)
    price = models.IntegerField()
    years = models.ForeignKey(Years, on_delete=models.CASCADE)
