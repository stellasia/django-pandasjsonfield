# django-pandasjsonfield

[![Build Status](https://travis-ci.org/stellasia/django-pandasjsonfield.svg)](https://travis-ci.org/stellasia/django-pandasjsonfield)


A custom django model field to handle pandas Series and DataFrame. 

Pandas objects are saved in JSON format in a Django TextField.


## Compatibility

Tested with :

- `django 1.8`
- `pandas 0.16.2`


## Usage

1. Create a model:

        class MyModel(models.Model):
            serie = PandasJSONField(typ="serie", null=True)
            dataframe = PandasJSONField(null=True)


2. Manipulate it as usual:

    	import pandas as pd
        s = pd.Series([1,2,3,4])
	df = pd.DataFrame( {"a":[1,2,3], "b":[11,12,13]} )
	m = MyModel(serie=s, dataframe=df)
	m.save()

        m = MyModel.objects.get(pk=1)
	print m.dataframe.describe() # m.dataframe is a pandas.DataFrame

    
