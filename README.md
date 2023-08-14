# MTN MOMO Gateway

The `momogateway` package provides a Python interface for interacting with the MomoGateway API. It allows you to easily create an API user, generate an API key, and obtain a bearer token for authentication.

## Installation

You can install the `momogateway` package using pip:

```bash
pip install momogateway
```

## Usage

```python
from momogateway import momogateway

baseURL = "YOUR_BASE_URL"
callbackHost = "YOUR_CALLBACK_HOST"
apiKey = "YOUR_API_KEY"
xTargetEnvironment = "YOUR_TARGET_ENVIRONMENT"

result = momogateway.generate(baseURL, callbackHost, apiKey, xTargetEnvironment)
print(result)
```

Replace the placeholders (`YOUR_BASE_URL`, `YOUR_CALLBACK_HOST`, `YOUR_API_KEY`, `YOUR_TARGET_ENVIRONMENT`) with your actual API and environment details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
