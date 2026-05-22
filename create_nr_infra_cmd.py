import configparser
import os

def create_infra_cmd(apiKey: str):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)
    
    ACCOUNT_ID = config.get('newrelic', 'account_id')
    
    cmd = f"""
    curl -Ls https://download.newrelic.com/install/newrelic-cli/scripts/install.sh | bash && sudo NEW_RELIC_API_KEY={apiKey} NEW_RELIC_ACCOUNT_ID={ACCOUNT_ID} /usr/local/bin/newrelic install -y
    """

    return cmd
