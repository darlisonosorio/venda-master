from rest_framework import viewsets
from rest_framework.decorators import action

from core import models, serializers, queries, filters


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
    filter_class = filters.ZoneFilterSet


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.ZoneSerializer

    @action(detail=False, methods=['GET'])
    def get_by_name(self, request, *args, **kwargs):
        name = request.query_params['name']
        queryset = queries.get_state_by_name(name=name)
        self.queryset = queryset
        return super(StateViewSet, self).list(request, *args, **kwargs)


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.select_related('state').all()
    serializer_class = serializers.ZoneSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.select_related('city', 'zone').all()
    serializer_class = serializers.DistrictSerializer
    filter_class = filters.DistrictFilterSet


class StockAddressViewSet(viewsets.ModelViewSet):
    queryset = models.StockAddress.objects.all()
    serializer_class = serializers.StockAddressSerializer


class MovementViewSet(viewsets.ModelViewSet):
    queryset = models.Movement.objects.all()
    serializer_class = serializers.MovementSerializer
    filter_class = filters.MovementFilterSet


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductFilterSet


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
