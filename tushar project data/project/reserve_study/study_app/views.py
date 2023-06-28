from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .serializer import Replacement_Reserves_Serializer, YearSerializer, Common_Expenses_Serializer
from .forms import Common_Expenses, Common_Expenses_year

@csrf_exempt
def calculation(request):
    # form = Reserve_Study()
    if request.method == "POST":
        data = request.POST
        print(data)

        common_ex = {}
        replacement_re = {}
        # y = YearSerializer(data = data["year"])
        # y.is_valid()
        # y.save()

        for i in data.keys():
            if "key" in i :
                # print(i.split("key")[1])
                if int(i.split("key")[1]) <= 100:
                    common_ex[data[i]] = data["value"+i.split("key")[1]]
                elif int(i.split("key")[1]) >= 500:
                    replacement_re[data[i]] = data["value"+i.split("key")[1]]
        
        c = Common_Expenses_Serializer(data = common_ex)
        c.is_valid()
        r = Replacement_Reserves_Serializer(data = replacement_re)
        r.is_valid()
        c.save()
        r.save()

        result = {}
        #calculation for common expenses
        result["Revenues"] = int(data['common_expenses Dues']) * int(data['number_units']) * 12
        result["Minus_Delinquent"] = result["Revenues"] * float(data["minus_delinquent_payment"])
        result["Gross_Profit"] = result["Revenues"] - result["Minus_Delinquent"]

        result["Common_Expenses_subtotal"] = sum(map(int,common_ex.values()))
        result["Common_Expenses_NET_Profit_Loss"] = result["Gross_Profit"] - result["Common_Expenses_subtotal"]

        #calculation for replacement reserves
        result["Reserve_Account_Expenses"] = sum(map(int, replacement_re.values()))
        result["Income_from_Reserve_Dues"] = (int(data['replacement_reserve_dues']) * int(data["number_units"])) * 12
        result["Reserves"] = 14560 + result["Income_from_Reserve_Dues"] - result["Reserve_Account_Expenses"]
        
        #total dues
        result["MY_Total_MONTHLY_Dues"] = sum(list((int(data["common_expenses Dues"]), int(data["replacement_reserve_dues"]))))

        print(data)
        print(result)
        return render(request, "index.html")

def start(request):
    return render(request, "index.html")

