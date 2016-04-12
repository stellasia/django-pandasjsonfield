# django-pandasjsonfield

[![Build Status](https://travis-ci.org/stellasia/django-pandasjsonfield.svg)](https://travis-ci.org/stellasia/django-pandasjsonfield)


A custom django model field to handle pandas Series and DataFrame. 

Pandas objects are saved in JSON format in a Django TextField.


## Compatibility

Tested with :

- `django>=1.4` (`django>=1.5` for `python>=3`)
- `pandas>=0.16` 


## Usage

1. Installation 

        pip install pandasjsonfield

2. Create a model:

        from pandasjsonfield import PandasJSONField

        class MyModel(models.Model):
            serie = PandasJSONField(typ="serie", null=True)
            dataframe = PandasJSONField(typ="frame", null=True)

    and migrate your database with usual django commands.

3. Manipulate it as usual:

        import pandas as pd
        
        s = pd.Series([1,2,3,4])
        df = pd.DataFrame({"a":[1,2,3], "b":[11,12,13]})
        m = MyModel(serie=s, dataframe=df)
        m.save()
        
        m = MyModel.objects.get(pk=1)
        print m.dataframe.describe() # m.dataframe is a pandas.DataFrame


## Changelog

### `1.0 => 1.?`

- Support for `django-1.9` and `pandas-0.18`

- Change the method for object json-serialization from `orient="index"` to `orient="split"` (see [pandas doc](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html) for more informations):
	- allows to save the `Series` name
	- fixes a bug in the data types in deserialization (see [this issue](https://github.com/pydata/pandas/issues/12866))
	- If you are upgrading from version `1.0`, the first time you read your object, they will be deserialized correctly and re-serialized with the new method. This should be a smooth transition but please report any issue you may have in the [issue tracker](https://github.com/stellasia/django-pandasjsonfield/issues).


## Inspiration 

I have taken (a lot of) inspiration or technical solutions from the following repos: 

- [django-jsonfield](https://github.com/bradjasper/django-jsonfield)
- [django-newsletter](https://github.com/dokterbob/django-newsletter/)

Thanks to their authors. 


## Want to contribute?

Do not hesitate to open an [issue](https://github.com/stellasia/django-pandasjsonfield/issues) or fork!
