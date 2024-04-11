from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.item_name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    supplier_rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.organization_name


class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    upload_date = models.DateField()
    signed = models.BooleanField()
    supplier = models.ManyToManyField(Supplier, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_file_path = models.FileField(upload_to="static/contracts/")

    def __str__(self):
        return f"document #{self.contract_id}"
