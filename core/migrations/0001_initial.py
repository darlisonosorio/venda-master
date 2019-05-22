# Generated by Django 2.2.1 on 2019-05-15 21:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54, unique=True)),
            ],
            options={
                'db_table': 'branch_office',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=104)),
                ('salary', models.DecimalField(db_column='nb_salary', decimal_places=4, max_digits=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], db_column='cs_gender', max_length=1)),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54, unique=True)),
            ],
            options={
                'db_table': 'departament',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54)),
                ('city', models.ForeignKey(db_column='id_city', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.City')),
            ],
            options={
                'db_table': 'district',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=104)),
                ('salary', models.DecimalField(db_column='nb_salary', decimal_places=4, max_digits=10)),
                ('admission_date', models.DateField(db_column='dt_admission')),
                ('date_birth', models.DateField(db_column='dt_birth')),
                ('departament', models.ForeignKey(db_column='id_departament', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Departament')),
                ('manager', models.ForeignKey(db_column='id_manager', db_index=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Employee')),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('description', models.CharField(db_column='tx_description', max_length=54, unique=True)),
            ],
            options={
                'db_table': 'marital_status',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MeansPayment',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('description', models.CharField(db_column='tx_description', max_length=54, unique=True)),
            ],
            options={
                'db_table': 'means_payment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('description', models.CharField(db_column='tx_description', max_length=54, unique=True)),
                ('commission_percentage', models.DecimalField(db_column='nb_commission_percentage', decimal_places=4, max_digits=10)),
                ('gain_percentage', models.DecimalField(db_column='nb_gain_percentage', decimal_places=4, max_digits=10)),
            ],
            options={
                'db_table': 'product_group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('date', models.DateTimeField(db_column='dt_sale', default=django.utils.timezone.now)),
                ('branch_office', models.ForeignKey(db_column='id_branch_office', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.BranchOffice')),
                ('customer', models.ForeignKey(db_column='id_customer', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Customer')),
                ('employee', models.ForeignKey(db_column='id_employee', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Employee')),
            ],
            options={
                'db_table': 'sale',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54)),
                ('abbreviation', models.CharField(db_column='tx_abbreviation', max_length=2)),
            ],
            options={
                'db_table': 'state',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54, unique=True)),
            ],
            options={
                'db_table': 'zone',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=54)),
                ('district', models.ForeignKey(db_column='id_district', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.District')),
            ],
            options={
                'db_table': 'supplier',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('quantity', models.DecimalField(db_column='nb_quantity', decimal_places=3, max_digits=10)),
                ('product', models.ForeignKey(db_column='id_product', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.ProductGroup')),
                ('sale', models.ForeignKey(db_column='id_sale', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sale')),
            ],
            options={
                'db_table': 'sale_item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=104)),
                ('cost_price', models.DecimalField(db_column='nb_cost_price', decimal_places=4, max_digits=10)),
                ('sale_price', models.DecimalField(db_column='nb_sale_price', decimal_places=4, max_digits=10)),
                ('product_group', models.ForeignKey(db_column='id_product_group', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.ProductGroup')),
                ('supplier', models.ForeignKey(db_column='id_supplier', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Supplier')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.ForeignKey(db_column='id_marital_status', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.MaritalStatus'),
        ),
        migrations.AddField(
            model_name='district',
            name='zone',
            field=models.ForeignKey(db_column='id_zone', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Zone'),
        ),
        migrations.AddField(
            model_name='customer',
            name='district',
            field=models.ForeignKey(db_column='id_district', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.District'),
        ),
        migrations.AddField(
            model_name='customer',
            name='marital_status',
            field=models.ForeignKey(db_column='id_marital_status', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.MaritalStatus'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='id_state', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.State'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='district',
            field=models.ForeignKey(db_column='id_district', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.District'),
        ),
        migrations.AddIndex(
            model_name='supplier',
            index=models.Index(fields=['district'], name='supplier_id_dist_fe5872_idx'),
        ),
        migrations.AddIndex(
            model_name='saleitem',
            index=models.Index(fields=['sale'], name='sale_item_id_sale_2fb28d_idx'),
        ),
        migrations.AddIndex(
            model_name='saleitem',
            index=models.Index(fields=['product'], name='sale_item_id_prod_17dc4f_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['employee'], name='sale_id_empl_022ef8_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['branch_office'], name='sale_id_bran_b9678a_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['customer'], name='sale_id_cust_e5ac89_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_group'], name='product_id_prod_0cee1f_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['supplier'], name='product_id_supp_6974a2_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['departament'], name='employee_id_depa_24033d_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['marital_status'], name='employee_id_mari_e2e04f_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['manager'], name='employee_id_mana_1b08b5_idx'),
        ),
        migrations.AddIndex(
            model_name='district',
            index=models.Index(fields=['city'], name='district_id_city_e3d0af_idx'),
        ),
        migrations.AddIndex(
            model_name='district',
            index=models.Index(fields=['zone'], name='district_id_zone_e0598f_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['marital_status'], name='customer_id_mari_0dcd0a_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['district'], name='customer_id_dist_a40d38_idx'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['state'], name='city_id_stat_55598a_idx'),
        ),
        migrations.AddIndex(
            model_name='branchoffice',
            index=models.Index(fields=['district'], name='branch_offi_id_dist_8858bb_idx'),
        ),
    ]