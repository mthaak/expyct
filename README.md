# Expyct

[![CircleCI](https://circleci.com/gh/HummingbirdTechGroup/expyct/tree/main.svg?style=svg)](https://circleci.com/gh/HummingbirdTechGroup/expyct/tree/main)

Partial matching of any object. This is especially useful for testing that your functions return expected values.


**Full reference can be found [here](https://hummingbirdtechgroup.github.io/expyct/).**

Example:

```python
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

```
