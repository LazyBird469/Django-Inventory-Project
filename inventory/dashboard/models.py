from django.db import models

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Eletronics', 'Eletronics'),
    ('Food', 'Food'),
)

class Product(models.Model): 
    name = models.CharField(max_length=100, null=True)
    category = models.ChatField(max_legrth=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)