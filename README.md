# py_cnab_api_client

Lightweight Python client and models for interacting with a CNAB-style API used in this workspace.

## Features

- Pydantic-based configuration and models
- Small, focused client for API requests
- Designed for local editable development (works well as a path dependency)

## Installation

Recommended: use Poetry and add this package as a path dependency (editable / develop mode) from the consuming project.

From the consuming project root (example `aeroclube_api`):

```bash
# Add as a path dependency in pyproject.toml:
# py_cnab_api_client = { path = "../py_cnab_api_client", develop = true }

poetry install
```

Or install locally into the active virtual environment for quick testing:

```bash
# from this package root
poetry run pip install -e .
```

If you don't use Poetry, you can use pip in an active venv:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## Quick Usage

Example using the minimal `ApiConfig` and `Client` provided by the package:

```python
from py_cnab_api_client import ApiConfig, Client

config = ApiConfig(base_url="https://api.example.com", timeout_seconds=30)
client = Client(config)

# use client methods (example)
# resp = client.get_boleto(123)
```

See the `py_cnab_api_client` package modules for available models and client methods.

## Development & Testing

- Run tests with pytest (from repository root or within the package folder):

```bash
poetry run pytest -q
```

- While developing, an editable installation (`pip install -e .`) or Poetry path dependency with `develop = true` is recommended so changes in the source tree are immediately visible to consumers.

## Contributing

Feel free to open issues or PRs. Keep changes small and add tests for logic changes.

## License

This project is licensed under the MIT License — see `LICENSE` for details.
