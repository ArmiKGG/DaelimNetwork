from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from djmoney.models.fields import MoneyField


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='RUB')
    classifier_name = models.CharField(max_length=255)
    classifier_code = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name


class Supplier(models.Model):
    organization_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    supplier_rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    items = models.ManyToManyField(Item, blank=True)
    classifier_name = models.CharField(max_length=255)
    classifier_code = models.CharField(max_length=255)

    def __str__(self):
        return self.organization_name


class Contract(models.Model):
    upload_date = models.DateField()
    signed = models.BooleanField()
    supplier = models.ManyToManyField(Supplier, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_file_path = models.FileField(upload_to="static/contracts/")

    def __str__(self):
        return f"document #{self.document_file_path}"


class Deliver(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def __str__(self):
        return f"deliverer #{self.supplier.name}"


class Directorer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    data = models.TextField()


class Finance(models.Model):
    file = models.FileField(upload_to="static")
