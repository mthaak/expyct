<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![CircleCI][circleci-shield]][circleci-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Expyct</h3>

  <p align="center">
    Partial matching of any Python object.
    <br />
    <a href="https://hummingbirdtechgroup.github.io/expyct/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HummingbirdTechGroup/expyct/issues">Report Bug</a>
    ·
    <a href="https://github.com/HummingbirdTechGroup/expyct/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">Expyct</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Expyct

<span style="font-size:larger;">_Partial matching of any Python object._</span>

```python
import expyct as exp


def test_my_function():
    result = my_function()

    assert result == exp.Float(optional=True, close_to=0.076, error=0.01)
```

Using Expyct is a good idea when you need to assert something in a test case but there is some non-determinism.

For example, rounding errors prevent you from comparing a `float` exactly. Or a timestamp is created on-the-fly, and therefore changes every test run.

In these cases, you need to be able to set specific constraints on the expected value. That is what Expyct is for!

The constraints can be provided as constructor arguments. For example `n == Number(min=3, max=5)` is only true when `n` is between 3 and 5.

Some other examples of classes are `Float`, `String`, `Any` and `DateTime`. As you can see, they closely match the built-in Python types.

The library also comes with many commonly used data validators like `ANY_UUID` which matches any UUID string. And `TODAY` which matches any datetime occurring on the current day.

Checking nested data structures is easy as well.

See [Usage examples](#usage)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Supported and tested for:
- Python 3.6
- Python 3.7
- Python 3.8
- Python 3.9

### Installation

```shell
pip install expyct
```

Or install using any Python package manager like conda, pipenv or poetry.

<!-- USAGE EXAMPLES -->
## Usage

See below examples of how to use Expyct with [pytest](https://docs.pytest.org/).

Simple example:

```python
import expyct as exp
from myclass import MyClass


def test_my_function():
    result = my_function()

    assert result == exp.AnyValue(instance_of=MyClass, vars={"property": "value"})
```

More complicated nested example:

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


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/HummingbirdTechGroup/expyct/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Bump the version in `expyct/__version__.py` following [SemVer](https://semver.org/)
5. Push the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Before starting to contribute to Expyct, please install [pre-commit](https://pre-commit.com) to make sure your
changes get checked for style and standards before committing them to repository:

    $ pre-commit install

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Please file an issue on Github.


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[circleci-shield]: https://circleci.com/gh/HummingbirdTechGroup/expyct/tree/main.svg?style=shield
[circleci-url]: https://circleci.com/gh/HummingbirdTechGroup/expyct/tree/main
[contributors-shield]: https://img.shields.io/github/contributors/HummingbirdTechGroup/expyct.svg?style=svg
[contributors-url]: https://github.com/HummingbirdTechGroup/expyct/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HummingbirdTechGroup/expyct.svg?style=svg
[forks-url]: https://github.com/HummingbirdTechGroup/expyct/network/members
[stars-shield]: https://img.shields.io/github/stars/HummingbirdTechGroup/expyct.svg?style=svg
[stars-url]: https://github.com/HummingbirdTechGroup/expyct/stargazers
[issues-shield]: https://img.shields.io/github/issues/HummingbirdTechGroup/expyct.svg?style=svg
[issues-url]: https://github.com/HummingbirdTechGroup/expyct/issues
[license-shield]: https://img.shields.io/github/license/HummingbirdTechGroup/expyct.svg?style=svg
[license-url]: https://github.com/HummingbirdTechGroup/expyct/blob/master/LICENSE
