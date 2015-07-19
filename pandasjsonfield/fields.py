from django.db import models
from django.core.exceptions import ValidationError

import pandas as pd


class PandasJSONField(models.TextField):
    """ Pandas Series or distribution 
    saved in JSON format in a TextField. 
    
    Additionnal parameter : `typ` = 'serie'|'frame' 
    (if not specified, use the pandas default, 
    currently 'frame' in version 0.16.2)
    """

    def __init__(self, *args, **kwargs):
        try:
            self._typ = kwargs.pop("typ")
        except KeyError:
            self._typ = 'frame'
        super(PandasJSONField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(PandasJSONField, self).deconstruct()
        kwargs["typ"] = self._typ
        return name, path, args, kwargs

    # Convert text field (value) to python object
    def from_db_value(self, value, expression, connection, context):
        print "from_db_value", value
        if value is None:
            return value
        return pd.read_json(value, typ=self._typ)

    def to_python(self, value):
        print "to_python", value
        if value is None:
            return value
        if isinstance(value, pd.Series):
            return value        
        try:
            return pd.read_json(value, typ=self._typ)
        except:
            raise ValidationError("Not a valid pandas type")

    # convert python object to db type
    def get_prep_value(self, value):
        print "get_prep_value"
        if value :
            return value.to_json()
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        """Convert JSON object to a string"""
        print "get_db_prep_value", value
        if self.null and value is None:
            return None
        return value.to_json()
