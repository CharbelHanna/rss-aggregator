import os
import io
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient
from azure.keyvault.secrets import SecretClient

#configuration
    #Azure Blob Storage Account Information
BLOB_account = 'rssblobstg01'
BLOB_container = '$web'
BLOB_name = 'aws.rss'

#Azure File Share information
FS_fsname = 'rsslist.txt'

#keyvault information
KV_account = 'rss-kv-01'
KV_secret_name = 'rssblobstg01key'

# Print datetime and environment variables
print(f'{datetime.now()}')
print(f'This is an environment variable: {os.environ.get("public1")}')
print(f'This is a secret environment variable: {os.environ.get("private1")}')

# Authenticate with Azure
# (1) environment variables, (2) Managed Identity, (3) User logged in in Microsoft application, ...
AZ_credential = DefaultAzureCredential()

# Retrieve primary key for blob from the Azure Keyvault
KV_url = f'https://{KV_account}.vault.azure.net'
KV_secretClient = SecretClient(vault_url=KV_url, credential=AZ_credential)
BLOB_PrimaryKey = KV_secretClient.get_secret(KV_secret_name).value