# Generated by Django 5.0.6 on 2024-07-20 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulas', '0005_formula_icon_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formula',
            old_name='formula',
            new_name='link',
        ),
    ]
