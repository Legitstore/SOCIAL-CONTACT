# Generated by Django 4.2.4 on 2023-08-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='relation',
            field=models.CharField(blank=True, choices=[('Family', 'Family'), ('Friend', 'Friend'), ('Cousin', 'Cousin'), ('In-Law', 'In-Law'), ('Others', 'Others')], max_length=100, null=True),
        ),
    ]
