from sqlalchemy import Column, String, Text, Boolean, ForeignKey, DateTime, CheckConstraint, func,Enum
from sqlalchemy.dialects.postgresql import UUID
from extensions import db
from base.models import BaseModel
from sqlalchemy.dialects.postgresql import ENUM as PGEnum



alert_type_enum = PGEnum(
    'cost risk signals', 'sentiment signals', 'onboarding escallation',
    name='alert_type_enum',
    create_type=False
)

alert_category_enum = PGEnum(
    'Sentiment', 'Risk', 'Opportunity', 'Delegation', 'Escalation',
    name='alert_category_enum',
    create_type=False
)

alert_tag_enum = PGEnum(
    'Critical', 'High', 'Medium', 'Low',
    name='alert_tag_enum',
    create_type=False
)

class Alert(BaseModel):
    __tablename__ = 'alerts'

    customer_id = db.Column(db.String(40), db.ForeignKey('customers.id', ondelete='CASCADE'), primary_key=True)
    category = Column(alert_category_enum, nullable=True)
    tag = Column(alert_tag_enum, nullable=True)
    type = Column(alert_type_enum, nullable=True)
    title = db.Column(db.Text, nullable=True)
    message = db.Column(db.Text, nullable=True)
    raised_by = db.Column(db.String(40), nullable=True)
    is_new = db.Column(db.Boolean, default=True, nullable=False)