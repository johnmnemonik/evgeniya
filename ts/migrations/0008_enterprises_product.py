# Generated by Django 2.2.4 on 2019-08-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0007_auto_20190818_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprises',
            name='product',
            field=models.ManyToManyField(to='ts.Product', verbose_name='продукты'),
        ),
    ]
