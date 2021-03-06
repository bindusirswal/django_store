# Generated by Django 3.0.1 on 2020-01-08 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=250)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='INR Order Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=250, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=250)),
                ('billingAddress1', models.CharField(blank=True, max_length=250)),
                ('billingCity', models.CharField(blank=True, max_length=250)),
                ('billingPostcode', models.CharField(blank=True, max_length=250)),
                ('billingCountry', models.CharField(blank=True, max_length=250)),
                ('ShippingName', models.CharField(blank=True, max_length=250)),
                ('ShippingAddress1', models.CharField(blank=True, max_length=250)),
                ('ShippingCity', models.CharField(blank=True, max_length=250)),
                ('ShippingPostcode', models.CharField(blank=True, max_length=250)),
                ('ShippingCountry', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='INR Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
