# sample-azure-python

## Running this sample
1.  If you don't already have it, [install Python](https://www.python.org/downloads/).

    This sample (and the SDK) is compatible with Python 2.7, 3.4, 3.5, 3.6 and 3.7.

2.  General recommendation for Python development is to use a Virtual Environment.
    For more information, see https://docs.python.org/3/tutorial/venv.html

    Install and initialize the virtual environment with the "venv" module on Python 3 (you must install [virtualenv](https://pypi.python.org/pypi/virtualenv) for Python 2.7):

    ```
    python -m venv mytestenv # Might be "python3" or "py -3.6" depending on your Python installation
    cd mytestenv
    source bin/activate      # Linux shells (Bash, ZSH, etc.)
    scripts\activate         # Windows shells (PowerShell, CMD)
    ```

3.  Clone the repository.

    ```
    git clone https://github.com/Azure-Samples/virtual-machines-python-manage.git
    ```

4.  Install the dependencies using pip.

    ```
    cd virtual-machines-python-manage
    pip install -r requirements.txt
    ```

5.  Create an Azure service principal either through
[Azure CLI](http://azure.microsoft.com/documentation/articles/resource-group-authenticate-service-principal-cli/),
[PowerShell](http://azure.microsoft.com/documentation/articles/resource-group-authenticate-service-principal/)
or [the portal](http://azure.microsoft.com/documentation/articles/resource-group-create-service-principal-portal/).

    Retrieve the application ID (a.k.a. client ID),
    authentication key (a.k.a. client secret),
    tenant ID and subscription ID from the Azure portal for use
    in the next step.
    [This document](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
    describes where to find them (besides the subscription ID,
    which is in the "Overview" section of the "Subscriptions" blade.)

6.  Fill in and export these environment variables into your current shell.

    ```
    export AZURE_TENANT_ID={your tenant id}
    export AZURE_CLIENT_ID={your client id}
    export AZURE_CLIENT_SECRET={your client secret}
    export AZURE_SUBSCRIPTION_ID={your subscription id}
    ```

7.  Run the sample.

    ```
    python example.py
    ```
