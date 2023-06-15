# Generated by Django 4.0 on 2023-06-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('se_function', '0003_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('按摩椅', '按摩椅')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('可購買', '可購買'), ('缺貨', '缺貨')], max_length=50),
        ),
    ]
