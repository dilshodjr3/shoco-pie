# Generated by Django 5.1.5 on 2025-01-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choco', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FastContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Tez aloqa',
            },
        ),
    ]
