import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.network import NetworkManagementClient

#Parameter
GROUP_NAME = 'MyResourceGroup'
NIC_NAME = 'ipconfig1'
PRIVATE_IPADDRESS = '192.168.10.14'

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

    # Get NetworkInterface by name
    print('Get Current NetworkInterface by Name')
    network_interface =  network_client.network_interfaces.get(GROUP_NAME, NIC_NAME)
    #Update Network Interface
    network_interface.ip_configurations[0].private_ip_address = PRIVATE_IPADDRESS 
    network_interface.ip_configurations[0].private_ip_allocation_method = "static"
    print('Update NIC')
    async_nic_creation = network_client.network_interfaces.create_or_update(
        GROUP_NAME,
        NIC_NAME,
        network_interface
    )

if __name__ == "__main__":
    run_example()
