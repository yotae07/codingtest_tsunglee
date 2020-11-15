from django.db   import models

from user.models import User

class Image(models.Model):
    main_image   = models.CharField(max_length=200)
    sub_image    = models.CharField(max_length=200)
    detail_image = models.CharField(max_length=200)
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'

class Product(models.Model):
    name       = models.CharField(max_length=200)
    price      = models.IntegerField()
    image      = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

class Order(models.Model):
    product    = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
