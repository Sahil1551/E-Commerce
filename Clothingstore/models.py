from django.db import models
from django.db.models import Model


# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    sub_category=models.CharField(max_length=50)
    prize=models.CharField(max_length=10)
    desc=models.CharField(max_length=1000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="images/products")
    def __str__(self):
        return self.product_name
class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class checkout(models.Model):
    p_id = models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country=models.CharField(max_length=10)
    size=models.IntegerField()
    Address = models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postcode=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField(max_length=254)
    notes=models.CharField(max_length=10000)
    answer=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

