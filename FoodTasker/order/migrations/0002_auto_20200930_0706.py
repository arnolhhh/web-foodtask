# Generated by Django 3.1.1 on 2020-09-30 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='order.order'),
        ),
    ]