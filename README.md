# Expyct

Partial matching of any object. This is especially useful for testing that your functions return expected values.

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
            "amount": exp.Float(min=3.5),
            "purchases": exp.List(of=exp.Dict(), not_empty=True),
        },
        "time_of_purchase": exp.OneOf([exp.TODAY, exp.THIS_WEEK]),
        "type": exp.AnyType(subclassof=str),
        "item_ids": exp.Set([1, 2, 3], subset=True),
        "context": exp.ANY,
    }

```
