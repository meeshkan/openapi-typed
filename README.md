# OpenAPI typed

[![github](https://github.com/Meeshkan/openapi-typed/workflows/Python%20build/badge.svg)](https://github.com/Meeshkan/openapi-typed/actions)
[![PyPI](https://img.shields.io/pypi/dm/openapi-typed.svg)](https://pypi.org/project/openapi-typed/)
[![PyPi](https://img.shields.io/pypi/pyversions/openapi-typed)](https://pypi.org/project/openapi-typed/)
[![License](https://img.shields.io/pypi/l/openapi-typed)](LICENSE)

Python typings for [OpenAPI](https://swagger.io/specification/) using [TypedDict](https://www.python.org/dev/peps/pep-0589/).

## Installation

Install package from [PyPI](https://pypi.org/project/openapi-typed/).

```bash
pip install openapi-typed
```

## Usage

```python
from openapi_typed import OpenAPIObject, Info

# Valid OpenAPIObject
openapi_valid = OpenAPIObject(
    openapi="3.0.0",
    info=Info(
        title="My API",
        version="0.0.0")
    )

# Invalid OpenAPIObject
openapi_invalid = OpenAPIObject(
    openap="3.0.0",  # Type-check error, unknown attribute
    info=Info(
        title="My API"  # Type-check error, missing attribute `version`
    )
)
```

## Development

Install development dependencies:

```bash
pip install -e .[dev]
```

Run tests:

```bash
pytest
# OR
python setup.py test
```

Run type-checks with `mypy`:

```bash
mypy openapi_typed
```

Build package:

```bash
python setup.py dist
```

## Contributing

Thanks for wanting to contribute! We will soon have a contributing page
detaling how to contribute. Meanwhile, feel free to star this repository, open issues and ask for more features and support.

Please note that this project is governed by the [Meeshkan Community Code of Conduct](https://github.com/meeshkan/code-of-conduct). By participating in this project, you agree to abide by its terms.
