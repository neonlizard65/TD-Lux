from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    volume = models.FloatField(verbose_name="Объем (л)")
    category = models.CharField(max_length=25, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена")
    photo = models.ImageField(verbose_name="Фото", null=True, upload_to="media")
    count = models.IntegerField(verbose_name="Кол-во")
    
    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")
        
    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
    
class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 1, 'Клиент'
        MANAGER = 2, 'Менеджер'
        
    role = models.PositiveSmallIntegerField(choices = Role.choices, verbose_name="Роль", default=Role.MANAGER)
    name = models.CharField(max_length=30, verbose_name="Наименование")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    adress = models.CharField(max_length=150, verbose_name="Адрес")
    
class Sklad(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    adress = models.CharField(max_length=150, verbose_name="Адрес")
    products = models.ManyToManyField(Product, verbose_name="Товары", related_name="sklad_product")
    
    class Meta:
        verbose_name = _("Склад")
        verbose_name_plural = _("Склады")
        
    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
        

    
class Zayavka(models.Model):
    date = models.DateTimeField(verbose_name="Дата заявки")
    sum = models.FloatField(verbose_name="Сумма")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    employee = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Менеджер", null=True, related_name="manager_zayavka")
    client = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name=" Клиент", null=True, related_name="client_zayavka")
    
    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        
    def __repr__(self) -> str:
        return f"{self.client.name} {self.date}"
    
    def __str__(self) -> str:
        return f"{self.client.name} {self.date}"

    
    
    
    

    