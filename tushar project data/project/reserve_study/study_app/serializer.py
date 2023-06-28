from rest_framework import serializers
from .models import Years, Common_Expenses, Replacement_Reserves

class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Years
        field = "__all__"

class Common_Expenses_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Common_Expenses
        field = "__all__"

class Replacement_Reserves_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Replacement_Reserves
        field = "__all__"


