# Generated by Django 3.2.8 on 2021-12-15 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0025_auto_20211215_1928"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="service_plan_ref",
            new_name="inventory_service_plan_ref",
        ),
        migrations.RenameField(
            model_name="serviceplan",
            old_name="service_plan_ref",
            new_name="inventory_service_plan_ref",
        ),
    ]