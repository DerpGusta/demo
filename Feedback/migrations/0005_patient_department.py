# Generated by Django 2.2.2 on 2020-02-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0004_hod'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='department',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
