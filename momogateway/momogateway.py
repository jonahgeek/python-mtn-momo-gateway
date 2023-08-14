import requests
import uuid

def generate(baseURL, callbackHost, apiKey, xTargetEnvironment):
    xReferenceId = str(uuid.uuid4())

    headers = {
        "X-Reference-Id": xReferenceId,
        "Ocp-Apim-Subscription-Key": apiKey,
    }

    body = {
        "providerCallbackHost": callbackHost,
    }

    try:
        # Step 1: Create API User
        response = requests.post(f"{baseURL}/v1_0/apiuser", json=body, headers=headers)
        response.raise_for_status()

        apiHeaders = {
            "Ocp-Apim-Subscription-Key": apiKey,
        }

        # Step 2: Create API Key
        apiKeyResponse = requests.post(
            f"{baseURL}/v1_0/apiuser/{xReferenceId}/apikey", headers=apiHeaders
        )
        apiKeyValue = apiKeyResponse.json().get("apiKey")

        # Step 3: Create Bearer Token
        authConfig = {
            "username": xReferenceId,
            "password": apiKeyValue,
        }

        tokenHeaders = {
            "Ocp-Apim-Subscription-Key": apiKey,
            "X-Target-Environment": xTargetEnvironment,
        }

        tokenResponse = requests.post(
            f"{baseURL}/collection/token/",
            auth=(xReferenceId, apiKeyValue),
            headers=tokenHeaders,
        )
        tokenData = tokenResponse.json()
        token = tokenData.get("access_token")
        token_expires_in = tokenData.get("expires_in")

        return {
            "apiKey": apiKeyValue,
            "ocp_apim_subscription_key": apiKey,
            "x_reference_id": xReferenceId,
            "token": token,
            "token_expires_in": token_expires_in,
        }
    except requests.exceptions.RequestException as error:
        raise error

# Example usage
# baseURL = "YOUR_BASE_URL"
# callbackHost = "YOUR_CALLBACK_HOST"
# apiKey = "YOUR_API_KEY"
# xTargetEnvironment = "YOUR_TARGET_ENVIRONMENT"
# result = momogateway(baseURL, callbackHost, apiKey, xTargetEnvironment)
# print(result)
