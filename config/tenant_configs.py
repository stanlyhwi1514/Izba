import os
from dotenv import load_dotenv

load_dotenv()

TENANT_DATABASES = {
    "tenant1": os.getenv("TENANT_DATABASES_TENANT1"),
    "tenant2": os.getenv("TENANT_DATABASES_TENANT2"),
}