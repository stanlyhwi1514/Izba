from flask import request
from sqlalchemy import create_engine
from config import Config as config
from pymongo import MongoClient

_engine_registry = {}
_mongo_registry = {}

def get_tenant_name():
    tenant = request.headers.get("X-Tenant-ID")
    if not tenant:
        raise Exception("Missing tenant header")
    if tenant not in config.TENANT_DATABASES:
        raise Exception("Invalid tenant")
    return tenant

def get_tenant_engine():
    tenant = get_tenant_name()
    if tenant not in _engine_registry:
        _engine_registry[tenant] = create_engine(config.TENANT_DATABASES[tenant])
    return _engine_registry[tenant]



def get_tenant_mongo_db_engine():
    tenant = get_tenant_name()  # already handles validation
    if tenant not in _mongo_registry:
        client = MongoClient(config.TENANT_MONGODB_URIS[tenant])
        db_name = config.TENANT_MONGODB_URIS[tenant].rsplit("/", 1)[-1]
        _mongo_registry[tenant] = client[db_name]
    return _mongo_registry[tenant]

