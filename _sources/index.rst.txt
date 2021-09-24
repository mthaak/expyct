Expyct
======

*Partial matching of any Python object.*

Using Expyct is a good idea when you need to assert something in a test case but there is some non-determinism.

For example, rounding errors prevent you from comparing a :code:`float` exactly. Or a timestamp is created on-the-fly, and therefore changes every test run.

In these cases, you need to be able to set specific constraints on the expected value. That is what Expyct is for!

The constraints can be provided as constructor arguments. For example :code:`n == Number(min=3, max=5)` is only true when :code:`n` is between 3 and 5.

Some other examples of classes are :code:`Float`, :code:`String`, :code:`Any` and :code:`DateTime`. As you can see, they closely match the built-in Python types.

The library also comes with many commonly used data validators like :code:`ANY_UUID` which matches any UUID string. And :code:`TODAY` which matches any `datetime` occurring on the current day.

Checking nested data structures is easy as well:

.. code-block:: python

    import expyct as exp
    from datetime import datetime


    def test_my_function():
        result = my_function()

        assert result == {
            "first_name": exp.String(regex="(mary)|(peter)", ignore_case=True),
            "last_name": "Johnson",
            "signup_date": exp.DateTime(after=datetime(2020, 1, 2), before=datetime(2020, 3, 5)),
            "details": {
                "number": exp.Int(min=2),
                "amount": exp.Float(close_to=2.3, error=0.001),
                "purchases": exp.List(exp.Dict(keys={"id", "product", "category"}), non_empty=True),
            },
            "time_of_purchase": exp.OneOf([exp.TODAY, exp.THIS_HOUR]),
            "type": exp.AnyType(subclass_of=str),
            "item_ids": exp.Set(subset_of=[1, 2, 3]),
            "metadata": exp.Dict(keys_any=exp.Collection(superset_of=["a", "b"])),
            "context": exp.ANY,
        }

Submodules
----------

.. toctree::
   :maxdepth: 4

   expyct.any
   expyct.base
   expyct.collection
   expyct.combination
   expyct.datetime
   expyct.number
   expyct.string
