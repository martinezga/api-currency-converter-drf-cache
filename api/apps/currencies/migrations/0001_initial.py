# Generated by Django 3.2.16 on 2022-11-08 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('code', models.CharField(max_length=16, unique=True, verbose_name='currency code')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('updated', 'Updated'), ('error', 'error')], default='created', max_length=16)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies_currencymodel_creator_user', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currencies_currencymodel_modifier_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'currencies',
                'ordering': ['code'],
            },
        ),
    ]
