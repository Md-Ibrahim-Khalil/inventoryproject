from django.db import models

# Create your models here.
# python3 manage.py makemigrations    
# python3 manage.py migrate  
# python3 manage.py createsuperuser

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.name}-{self.quantity}'


  