"""Create and manage virtual machines.

This script expects that the following environment vars are set:

AZURE_TENANT_ID: your Azure Active Directory tenant id or domain
AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
AZURE_CLIENT_SECRET: your Azure Active Directory Application Secret
AZURE_SUBSCRIPTION_ID: your Azure Subscription Id
"""
import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.storage import StorageManagementClient 
import azure.mgmt.storage.models

GROUP_NAME = '<YourResourceGroup>'
ACCOUNT_NAME = "<YourStorage>"

def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id

def run_example():
    credentials, subscription_id = get_credentials()
    storage_client = StorageManagementClient(credentials, subscription_id)

    params_update = azure.mgmt.storage.models.StorageAccountCreateParameters(
            sku=azure.mgmt.storage.models.Sku(name=azure.mgmt.storage.models.SkuName.standard_lrs),
            kind=azure.mgmt.storage.models.Kind.storage,
            location="japaneast",
            enable_https_traffic_only=True
        )

    result = storage_client.storage_accounts.update(GROUP_NAME, ACCOUNT_NAME, params_update)

if __name__ == "__main__":
    run_example()

