# Generated by Django 4.2.5 on 2023-09-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='caregory',
            new_name='category',
        ),
    ]
