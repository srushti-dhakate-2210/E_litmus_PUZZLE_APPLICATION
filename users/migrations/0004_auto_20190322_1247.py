# Generated by Django 2.1.7 on 2019-03-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190322_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='qstn_ans_on',
            field=models.DateTimeField(null=True),
        ),
    ]