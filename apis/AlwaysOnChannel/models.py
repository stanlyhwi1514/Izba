from sqlalchemy import Column, String, Text, Boolean, ForeignKey, DateTime, CheckConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from extensions import db
from base.models import BaseModel

class Alerts(BaseModel):
    __tablename__ = 'alerts'

    customer_id = db.Column(db.String(40), db.ForeignKey('customers.id', ondelete='CASCADE'), primary_key=True)
    type = db.Column(db.Text, nullable=False)
    severity = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=True)
    message = db.Column(db.Text, nullable=True)
    raised_by = db.Column(db.String(40), nullable=True)
    is_new = db.Column(db.Boolean, default=True, nullable=False)

    __table_args__ = (
        CheckConstraint(
            type.in_(['Sentiment', 'Risk', 'Opportunity', 'Delegation', 'Escalation']),
            name='check_type'
        ),
        CheckConstraint(
            severity.in_(['Critical', 'High', 'Medium', 'Low']),
            name='check_severity'
        ),
    )