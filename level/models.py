from django.db import models


class Value (models.Model):
    date_value=models.DateTimeField()

    level_value=models.FloatField(default=0)
    temp_value=models.CharField(max_length=10)
    package_value=models.IntegerField(default=0)
    power_value = models.CharField(max_length=10)

    class Meta:
        abstract = True


class Stan1 (Value):
    pass


class Stan2 (Value):
    pass


class Stan3 (Value):
    pass


class Stan4 (Value):
    pass

