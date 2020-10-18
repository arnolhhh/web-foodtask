# Generated by Django 3.1.1 on 2020-09-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On The Way'), (4, 'Delivered')], null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
