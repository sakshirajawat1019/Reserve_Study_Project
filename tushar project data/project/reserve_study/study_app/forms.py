from django import forms

class Common_Expenses(forms.Form):
    year = forms.IntegerField()
    common_expenses_dues = forms.IntegerField()


class Common_Expenses_year(forms.Form):
    number_of_units = forms.IntegerField()
    replacement_reserve_dues = forms.IntegerField()
    Bank_Fees = forms.IntegerField()
    Contractor_Repairs = forms.IntegerField()
    In_House_Maintenance = forms.IntegerField()
    Landscaping_Major = forms.IntegerField()
    Replacement_Reserve_Dues = forms.IntegerField()







