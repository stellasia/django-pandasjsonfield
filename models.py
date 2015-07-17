from django.db import models

from .fields import PandasJSONField


class MyData(models.Model):
    price = models.FloatField()
    evolution = PandasJSONField(typ="serie", null=True)
    distribution = PandasJSONField(null=True)
        
    def mean(self, column):
        try:
            return self.distribution[column].mean()
        except KeyError:
            return None

