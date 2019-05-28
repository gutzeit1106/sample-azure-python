import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.network import NetworkManagementClient

#Parameter
LOCATION = 'japaneast'
GROUP_NAME = 'MyResourceGroup'
IP_CONFIG_NAME = 'ipconfig1'
NIC_NAME = 'MyNIC'
PRIVATE_IPADDRESS = '10.0.0.12'
SUBNET_ID = '/subscriptions/xxxx/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/Mysubnet'


def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id

def run_example():
    #
    # Create all clients with an Application (service principal) token provider
    #
    credentials, subscription_id = get_credentials()
    network_client = NetworkManagementClient(credentials, subscription_id)

    #Update Network Interface
    print('Update NIC')
    async_nic_creation = network_client.network_interfaces.create_or_update(
        GROUP_NAME,
        NIC_NAME,
        {
            'location': LOCATION,
            'ip_configurations': [{
                'name': IP_CONFIG_NAME,
                "properties": {
                    "privateIPAddress": PRIVATE_IPADDRESS,
                    "privateIPAllocationMethod": "Static",
                     'subnet': {
                        'id': SUBNET_ID
                    }
                    }
                }
            ]
        }
    )

if __name__ == "__main__":
    run_example()
