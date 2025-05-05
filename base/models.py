import uuid

from sqlalchemy import Column, DateTime, String, func

from common.utils.json_utils import serialize
from extensions import db

def default_uuid():
    return uuid.uuid4().hex


class BaseModel(db.Model):
    __abstract__ = True

    __mapper_args__ = {
        'confirm_deleted_rows': False
    }
    
    id = Column(String(40), primary_key=True, default=lambda: default_uuid())
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    
    def _asdict(self):
        return serialize(self)

    def objects(*args):
        return db.session.query(*args)