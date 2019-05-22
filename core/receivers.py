from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from core import models


@receiver(post_save, sender=models.SaleItem, dispatch_uid="update_subtotal", weak=False)
def update_subtotal(sender, instance: models.SaleItem, created=False, **kwargs):
    if created:
        subtotal = instance.product.sale_price * instance.quantity
        instance.subtotal = subtotal
        instance.save()


@receiver(post_save, sender=models.Sale, dispatch_uid="create_sale_movement", weak=False)
def create_sale_movement(sender, instance: models.Sale, created=False, **kwargs):
    if created:
        try:
            models.Movement.objects.get(document=instance.pk)
        except models.Movement.DoesNotExist:
            payload = {
                'type': models.Movement.S,
                'date': now().date(),
                'address': models.StockAddress.objects.first(),
                'document': str(instance.pk)
            }
            models.Movement.objects.create(**payload)
        # movement = models.Movement()
        # movement.address = models.StockAddress.objects.first()
        # movement.document = instance.pk
        # movement.save()


@receiver(post_save, sender=models.SaleItem, dispatch_uid="create_movement_item", weak=False)
def create_movement_item(sender, instance: models.SaleItem, created=False, **kwargs):
    if created:
        movement = models.Movement.objects.get(document=instance.sale.pk)
        payload = {
            'movement': movement,
            'product': instance.product,
            'quantity': instance.quantity
        }
        models.MovementItem.objects.create(**payload)
