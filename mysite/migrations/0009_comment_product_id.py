# Generated by Django 4.2.5 on 2024-05-31 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.product'),
        ),
    ]
