# -*- coding: utf-8 -*-

import sys
import pandas as pd
import pandas.util.testing as pdt

from django.db import models
from django.test import TestCase
    
from .fields import PandasJSONField
from .models import MyModel


class PandasJSONField(TestCase):
    """
    pandasjsonfield tests
    """

    model = MyModel

    l = [1, 2, 3, 4]
    d = {"a": [1, 2, 3, 4],
         "b": [11, 12, 13, 14],
         "c": [21, 22, 23, 24]}

    def test_field_creation_series(self):
        """ Test saving a Series to a PandasJSONField
        """
        s = pd.Series(self.l)
        obj = self.model.objects.create(serie=s)
        new_obj = self.model.objects.get(pk=obj.pk)
        pdt.assert_series_equal(new_obj.serie, s)

    def test_field_creation_dataframe(self):
        """ Test saving a DataFrame to a PandasJSONField
        """
        df = pd.DataFrame(self.d)
        obj = self.model.objects.create(dataframe=df)
        new_obj = self.model.objects.get(pk=obj.pk)
        pdt.assert_frame_equal(new_obj.dataframe, df)

    def test_field_modify_series(self):
        """ Test updating a PandasJSONField """
        s = pd.Series(self.l)
        obj = self.model.objects.create(serie=s)
        pdt.assert_series_equal(obj.serie, s)

        s2 = pd.Series( [10, 11, 12] )
        obj.serie = s2

        pdt.assert_series_equal(obj.serie, s2)
        obj.save()
        pdt.assert_series_equal(obj.serie, s2)


    def test_field_modify_dataframe(self):
        """ Test updating a PandasJSONField """
        df = pd.DataFrame(self.d)
        obj = self.model.objects.create(dataframe=df)
        pdt.assert_frame_equal(obj.dataframe, df)

        df2 = pd.DataFrame( {"g": [10, 11, 12], "h": [20, 21, 22]} )
        obj.dataframe = df2

        pdt.assert_frame_equal(obj.dataframe, df2)
        obj.save()
        pdt.assert_frame_equal(obj.dataframe, df2)

