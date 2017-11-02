from django.db import models

# Create your models here.

class Stock(models.Model):
    pirce = 12345

    def get_price(self):
        return price
