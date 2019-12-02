# OpenAPI typed

Python typings for [OpenAPI](https://swagger.io/specification/) using [TypedDict](https://www.python.org/dev/peps/pep-0589/).

## Installation

```bash
pip install openapi_typed
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
