# Generated by Django 4.2.1 on 2023-05-13 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_client_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='client',
            name='login',
            field=models.CharField(max_length=25, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=25, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=25, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.FloatField(verbose_name='Объем (л)'),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='adress',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='products',
            field=models.ManyToManyField(to='webapp.product', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='date',
            field=models.DateTimeField(verbose_name='Дата заявки'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='products',
            field=models.ManyToManyField(to='webapp.product', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='sum',
            field=models.FloatField(verbose_name='Сумма'),
        ),
    ]