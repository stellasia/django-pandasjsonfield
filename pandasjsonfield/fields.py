from django.db import models
from django.core.exceptions import ValidationError
try:
    from django.utils import six
except ImportError:
    import six
import pandas as pd


class PandasJSONField(six.with_metaclass(models.SubfieldBase, models.TextField)):
    """ Pandas Series or distribution
    saved in JSON format in a TextField.

    Additionnal parameter : `typ` = 'serie'|'frame'
    """

    def __init__(self, *args, **kwargs):
        try:
            self._typ = kwargs.pop("typ")
        except KeyError:
            self._typ = None
        super(PandasJSONField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(PandasJSONField, self).deconstruct()
        kwargs["typ"] = self._typ
        return name, path, args, kwargs

    # Convert text field (value) to python object
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return pd.read_json(value, typ=self._typ)

    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, pd.Series) or isinstance(value, pd.DataFrame):
            return value
        try:
            return pd.read_json(value, typ=self._typ)
        except:
            raise ValidationError("Not a valid pandas type")

    # convert python object to db type
    def get_prep_value(self, value):
        if value:
            return value.to_json()
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        """Convert JSON object to a string"""
        if self.null and value is None:
            return None
        return value.to_json()
