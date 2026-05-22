import requests
import configparser
import os


def get_user_key():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    config.read(config_path)

    NERDGRAPH_ENDPOINT = "https://api.newrelic.com/graphql"
    API_KEY = config.get("newrelic", "api_key")
    ACCOUNT_ID = config.get("newrelic", "account_id")
    USER_ID = config.get("newrelic", "numeric_user_id")

    mutation = (
        """
    mutation {
    apiAccessCreateKeys(
        keys: {user: {accountId: """
        + ACCOUNT_ID
        + """, name: "Automated User Key", notes: "Created via automation script for querying NerdGraph.", userId: """
        + USER_ID
        + """}}

    ) {
        createdKeys {
        id
        key
        name
        notes
        type
        }
        errors {
        message
        type
        }
    }
    }
    """
    )
    headers = {"Content-Type": "application/json", "API-Key": API_KEY}
    payload = {"query": mutation}
    try:
        response = requests.post(NERDGRAPH_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()["data"]["apiAccessCreateKeys"]["createdKeys"][0]["key"]
        return result
    except requests.exceptions.RequestException as e:
        return e
