# django-pandasjsonfield

[![Build Status](https://travis-ci.org/stellasia/django-pandasjsonfield.svg)](https://travis-ci.org/stellasia/django-pandasjsonfield)


A custom django model field to handle pandas Series and DataFrame. 

Pandas objects are saved in JSON format in a Django TextField.


## Compatibility

Tested with :

- `django 1.4` (for `python < 3`) to `1.8` 
- `pandas>=0.16` (not tested for other versions but likely to work with [`pandas>=0.12`](http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#i-o-enhancements))


## Usage

1. Installation 

        pip install pandasjsonfield

2. Create a model:

        from pandasjsonfield import PandasJSONField

        class MyModel(models.Model):
            serie = PandasJSONField(typ="serie", null=True)
            dataframe = PandasJSONField(null=True)


3. Manipulate it as usual:

        import pandas as pd
        
        s = pd.Series([1,2,3,4])
        df = pd.DataFrame( {"a":[1,2,3], "b":[11,12,13]} )
        m = MyModel(serie=s, dataframe=df)
        m.save()
        
        m = MyModel.objects.get(pk=1)
        print m.dataframe.describe() # m.dataframe is a pandas.DataFrame


## INSPIRATION

I have taken (a lot of) inspiration or technical solutions from the following repos: 

- [django-jsonfield](https://github.com/bradjasper/django-jsonfield)
- [django-newsletter](https://github.com/dokterbob/django-newsletter/)
