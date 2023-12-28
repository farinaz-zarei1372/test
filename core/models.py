from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item.name


class ProductItemTransition(models.Model):
    status_choices = [("IMPORT", 'import'), ("EXPORT", 'export')]
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=status_choices, default=status_choices[0])
    transition_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_item.name

# Create your models here.
