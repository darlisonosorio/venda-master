# Generated by Django 2.2.1 on 2019-05-16 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190515_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(db_column='id_product', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Product'),
        ),
    ]