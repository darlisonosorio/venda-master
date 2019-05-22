from rest_framework import serializers
from core import models


class BaseSerializer(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class ZoneSerializer(BaseSerializer):
    class Meta:
        model = models.Zone
        fields = '__all__'


class StateSerializer(BaseSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class StateLightSerializer(BaseSerializer):
    class Meta:
        model = models.State
        fields = ['id', 'nome']


class CitySerializer(BaseSerializer):
    state_obj = StateLightSerializer(source='state', read_only=True, many=False)  # many=True atributo pode ser uma lista.

    class Meta:
        model = models.City
        fields = '__all__'


class DistrictSerializer(BaseSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class StockAddressSerializer(BaseSerializer):
    class Meta:
        model = models.StockAddress
        fields = '__all__'


class MovementSerializer(BaseSerializer):
    class Meta:
        model = models.Movement
        fields = '__all__'


class ProductGroupSerializer(BaseSerializer):
    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class ProductSerializer(BaseSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class SupplierSerializer(BaseSerializer):
    class Meta:
        model = models.Supplier
        fields = '__all__'
