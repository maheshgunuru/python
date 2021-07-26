from django.db import models


class Decimal(models.Model):
    number = models.DecimalField(max_digits=20, decimal_places=5)
    pre = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    pre1 = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    objects = models.manager


