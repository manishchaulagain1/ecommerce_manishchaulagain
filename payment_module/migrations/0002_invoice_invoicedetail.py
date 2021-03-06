# Generated by Django 4.0.4 on 2022-06-09 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField()),
                ('payment_date', models.DateTimeField()),
                ('total_amount', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_amount', models.FloatField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_module.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product')),
            ],
        ),
    ]
