from django.db.models import Q, CharField, Value, ExpressionWrapper, F, FloatField, Sum, Subquery, Count
from django.db.models.functions import Upper, Lower, Cast, LPad

from core import models as core_models


def query1():
    q2 = core_models.Product.objects.filter(name__startswith='a')
    q4 = core_models.Product.objects.values('id', 'nome')
    q5 = core_models.Product.objects.get(pk=5)
    q6 = core_models.Product.objects.order_by('-id').first()
    q7 = core_models.Product.objects.order_by('id').last()
    q8 = core_models.Product.objects.exists()
    q9 = core_models.Product.objects.count()
    q10 = core_models.Product.objects.filter(Q(id__gt=4) | Q(name__startswith='a'))
    return q2, q4, q5, q6, q7, q8, q9, q10


def query2():
    return core_models.Product.objects.values('name', 'product_group__description')


# def query3():
# return core_models.Product.objects
# .filter(Q(product_group__description='Limpeza') | Q(product_group__description='Bebidas'))

def query3():
    query = core_models.ProductGroup.objects.filter(description__in=['Limpeza', 'Bebidas'])
    return core_models.Product.objects.filter(product_group__in=query)


def query4():
    return core_models.Product.objects.filter(product_group__description__in=['Limpeza', 'Bebidas'])


def query5():
    return core_models.Product.objects.annotate(
        code=LPad(
            Cast('id', output_field=CharField()),
            6,
            Value('0')
        ),
        name_upper=Upper('name'),
        name_lower=Lower('name')
    ).values('code', 'name_upper', 'name_lower')


def query6():
    return core_models.Product.objects.annotate(
        custom_code=LPad(
            Cast('id', output_field=CharField()),
            6,
            Value('0')
        )
    ).annotate(
        gain_price=ExpressionWrapper(
            F('sale_price') - F('cost_price'),
            output_field=FloatField()
        )
    ).values('custom_code', 'name', 'gain_price')


def query7():
    return core_models.SaleItem.objects.annotate(
        code=LPad(
            Cast('product__id', output_field=CharField()),
            6,
            Value('0')
        ),
        sub_total=ExpressionWrapper(
            F('product__sale_price') * F('quantity'),
            output_field=FloatField()
        )
    ).values('code', 'product__name', 'quantity', 'product__sale_price', 'sub_total')


def query11():
    subquery = core_models.Product.all()
    queryset = core_models.ProductGroup.objects.annotate(
        sale_total=Subquery(subquery.values('subtotal'), output_field=FloatField())
    ).values(
        'description', 'sale_total'
    )
    return queryset


def query12():
    core_models.SaleItem.objects.select_related('product', 'product__product_group').values(
        'product__product_group__description'
    ).annotate(
        sale_total=Sum(ExpressionWrapper(
            F('quantity') * F('product__sale_price'), output_field=FloatField()
        ), output_field=FloatField())
    ).values('product__product_group__description', 'sale_total')


def gain_by_project_group(year: int):
    return core_models.SaleItem.objects.select_related('sale', 'product', 'product__product_group').annotate(
        subtotal=ExpressionWrapper(F('quantity') * F('product__sale_price'), output_field=FloatField())
    ).filter(sale__date__year=year).values('product__product_group__description').annotate(
        gain=Sum(ExpressionWrapper(
            F('subtotal') * F('product__product_group__gain_percentage') / Value(100), output_field=FloatField())
        ), output_field=FloatField()
    ).values('product__product_group__description', 'sale_total')


def total_customer_by_marital_status():
    return core_models.Customer.objects.select_related('matrital_status').values(
        'marital_status__description'
    ).annotate(counter=Count('id')).values('marital_status__description', 'counter')


def get_state_by_name(name):
    return core_models.State.objects.filter(name=name).all()
