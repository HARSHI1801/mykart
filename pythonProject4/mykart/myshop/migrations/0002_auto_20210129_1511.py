# Generated by Django 3.1.1 on 2021-01-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]
