# Generated by Django 3.0.6 on 2020-05-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('data_group', models.CharField(default=None, max_length=64)),
                ('data_size', models.CharField(default=None, max_length=64)),
                ('extras', models.CharField(default=None, max_length=64)),
                ('extras_price', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('name', models.CharField(default=None, max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('toppings', models.CharField(default=None, max_length=64)),
                ('user', models.CharField(default=None, max_length=64)),
            ],
        ),
    ]
