# Generated by Django 5.1.2 on 2024-10-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('phone_prefix', models.CharField(blank=True, max_length=5, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10)),
                ('contact_person', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('barangay_number', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
