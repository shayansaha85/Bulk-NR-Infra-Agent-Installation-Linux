


def create_infra_cmd(apiKey : str):
    cmd = f"""
    curl -Ls https://download.newrelic.com/install/newrelic-cli/scripts/install.sh | bash && sudo NEW_RELIC_API_KEY={apiKey} NEW_RELIC_ACCOUNT_ID=3774110 /usr/local/bin/newrelic install -y
    """

    return cmd