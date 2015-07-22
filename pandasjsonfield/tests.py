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

    # def test_json_field_load(self):
    #     """Test loading a JSON object from the DB"""
    #     json_obj_1 = {'a': 1, 'b': 2}
    #     obj = self.json_model.objects.create(json=json_obj_1)
    #     new_obj = self.json_model.objects.get(id=obj.id)

    #     self.assertEqual(new_obj.json, json_obj_1)

    # def test_json_list(self):
    #     """Test storing a JSON list"""
    #     json_obj = ["my", "list", "of", 1, "objs", {"hello": "there"}]

    #     obj = self.json_model.objects.create(json=json_obj)
    #     new_obj = self.json_model.objects.get(id=obj.id)
    #     self.assertEqual(new_obj.json, json_obj)

    # def test_empty_objects(self):
    #     """Test storing empty objects"""
    #     for json_obj in [{}, [], 0, '', False]:
    #         obj = self.json_model.objects.create(json=json_obj)
    #         new_obj = self.json_model.objects.get(id=obj.id)
    #         self.assertEqual(json_obj, obj.json)
    #         self.assertEqual(json_obj, new_obj.json)

    # def test_custom_encoder(self):
    #     """Test encoder_cls and object_hook"""
    #     value = 1 + 3j  # A complex number

    #     obj = JSONModelCustomEncoders.objects.create(json=value)
    #     new_obj = JSONModelCustomEncoders.objects.get(pk=obj.pk)
    #     self.assertEqual(value, new_obj.json)

    # def test_django_serializers(self):
    #     """Test serializing/deserializing jsonfield data"""
    #     for json_obj in [{}, [], 0, '', False, {'key': 'value', 'num': 42,
    #                                             'ary': list(range(5)),
    #                                             'dict': {'k': 'v'}}]:
    #         obj = self.json_model.objects.create(json=json_obj)
    #         new_obj = self.json_model.objects.get(id=obj.id)
    #         self.assert_(new_obj)

    #     queryset = self.json_model.objects.all()
    #     ser = serialize('json', queryset)
    #     for dobj in deserialize('json', ser):
    #         obj = dobj.object
    #         pulled = self.json_model.objects.get(id=obj.pk)
    #         self.assertEqual(obj.json, pulled.json)

    # def test_default_parameters(self):
    #     """Test providing a default value to the model"""
    #     model = JsonModel()
    #     model.json = {"check": 12}
    #     self.assertEqual(model.json, {"check": 12})
    #     self.assertEqual(type(model.json), dict)

    #     self.assertEqual(model.default_json, {"check": 12})
    #     self.assertEqual(type(model.default_json), dict)

    # def test_invalid_json(self):
    #     # invalid json data {] in the json and default_json fields
    #     ser = '[{"pk": 1, "model": "jsonfield.jsoncharmodel", ' \
    #         '"fields": {"json": "{]", "default_json": "{]"}}]'
    #     with self.assertRaises(DeserializationError) as cm:
    #         next(deserialize('json', ser))
    #     inner = cm.exception.args[0]
    #     self.assertTrue(isinstance(inner, ValidationError))
    #     self.assertEqual('Enter valid JSON', inner.messages[0])

    # def test_integer_in_string_in_json_field(self):
    #     """Test saving the Python string '123' in our JSONField"""
    #     json_obj = '123'
    #     obj = self.json_model.objects.create(json=json_obj)
    #     new_obj = self.json_model.objects.get(id=obj.id)

    #     self.assertEqual(new_obj.json, json_obj)

    # def test_boolean_in_string_in_json_field(self):
    #     """Test saving the Python string 'true' in our JSONField"""
    #     json_obj = 'true'
    #     obj = self.json_model.objects.create(json=json_obj)
    #     new_obj = self.json_model.objects.get(id=obj.id)

    #     self.assertEqual(new_obj.json, json_obj)


    # def test_pass_by_reference_pollution(self):
    #     """Make sure the default parameter is copied rather than passed by reference"""
    #     model = JsonModel()
    #     model.default_json["check"] = 144
    #     model.complex_default_json[0]["checkcheck"] = 144
    #     self.assertEqual(model.default_json["check"], 144)
    #     self.assertEqual(model.complex_default_json[0]["checkcheck"], 144)

    #     # Make sure when we create a new model, it resets to the default value
    #     # and not to what we just set it to (it would be if it were passed by reference)
    #     model = JsonModel()
    #     self.assertEqual(model.default_json["check"], 12)
    #     self.assertEqual(model.complex_default_json[0]["checkcheck"], 1212)

    # def test_normal_regex_filter(self):
    #     """Make sure JSON model can filter regex"""

    #     JsonModel.objects.create(json={"boom": "town"})
    #     JsonModel.objects.create(json={"move": "town"})
    #     JsonModel.objects.create(json={"save": "town"})

    #     self.assertEqual(JsonModel.objects.count(), 3)

    #     self.assertEqual(JsonModel.objects.filter(json__regex=r"boom").count(), 1)
    #     self.assertEqual(JsonModel.objects.filter(json__regex=r"town").count(), 3)

    # def test_save_blank_object(self):
    #     """Test that JSON model can save a blank object as none"""

    #     model = JsonModel()
    #     self.assertEqual(model.empty_default, {})

    #     model.save()
    #     self.assertEqual(model.empty_default, {})

    #     model1 = JsonModel(empty_default={"hey": "now"})
    #     self.assertEqual(model1.empty_default, {"hey": "now"})

    #     model1.save()
    #     self.assertEqual(model1.empty_default, {"hey": "now"})

