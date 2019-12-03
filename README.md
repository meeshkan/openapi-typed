# OpenAPI typed

[![CircleCI](https://circleci.com/gh/unmock/openapi-typed.svg?style=svg)](https://circleci.com/gh/unmock/openapi-typed)
[![PyPI](https://img.shields.io/pypi/dm/openapi-typed.svg)](https://pypi.python.org/pypi)

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

Build package:

```bash
python setup.py dist
```
