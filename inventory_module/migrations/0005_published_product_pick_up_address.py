# Generated by Django 5.1.1 on 2024-10-31 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0004_alter_product_inventory_total_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='published_product',
            name='pick_up_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]