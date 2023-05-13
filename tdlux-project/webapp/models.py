from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Employee(AbstractUser):
    pass
    
class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    adress = models.CharField(max_length=150, verbose_name="Адрес")
    login = models.CharField(max_length=25, verbose_name="Логин")
    password = models.CharField(max_length=25, verbose_name="Пароль")
    
    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")
    
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    volume = models.FloatField(verbose_name="Объем (л)")
    category = models.CharField(max_length=25, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена")
    
    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")
    
class Sklad(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    adress = models.CharField(max_length=150, verbose_name="Адрес")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    
    class Meta:
        verbose_name = _("Склад")
        verbose_name_plural = _("Склады")

    
class Zayavka(models.Model):
    date = models.DateTimeField(verbose_name="Дата заявки")
    sum = models.FloatField(verbose_name="Сумма")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE, verbose_name="Менеджер")
    
    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
    
    
    
    
    

    