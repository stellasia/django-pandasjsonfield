from django.db import models

from .fields import PandasJSONField


class MyModel(models.Model):
    serie = PandasJSONField(typ="serie", null=True)
    dataframe = PandasJSONField(null=True)
    
    def mean(self, column):
        try:
            return self.dataframe[column].mean()
        except KeyError:
            return None

