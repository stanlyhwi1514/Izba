from sqlalchemy import Column, String, Text, Boolean, ForeignKey, DateTime, func, CheckConstraint,Enum,Numeric
from sqlalchemy.orm import relationship
from extensions import db  # adjust if your db import is different
from base.models import BaseModel  # assuming your BaseModel is in models.base
import enum
class Tenant(BaseModel):
    __tablename__ = 'tenant'

    name = Column(Text, nullable=False, unique=True)
    domain = Column(Text, unique=True)

    customers = relationship('Customer', backref='tenant')
    users = relationship('User', backref='tenant')

class SourceEnum(enum.Enum):
    gmail = 'gmail'
    slack = 'slack'
    gong = 'gong'
    zoom = 'zoom'
    microsoft_team = 'microsoft team'
    sales_force = 'sales force'

class Customer(BaseModel):
    __tablename__ = 'customers'

    name = Column(Text, nullable=False)
    industry = Column(Text)
    renewal_date = Column(DateTime(timezone=True), server_default=func.now(), index=True) 
    net_revenue_retention = Column(Numeric)  
    total_revenue = Column(Numeric)
    source = Column(Enum(SourceEnum), nullable=True)
    alerts = relationship('Alert', backref='customer',)

class TeamEnum(enum.Enum):
    accounts_team = 'accounts team'
    customer_team = 'initiative team'

class User(BaseModel):
    __tablename__ = 'users'

    email = Column(Text, nullable=False, unique=True)
    full_name = Column(Text)
    password_hash = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    team = Column(Enum(TeamEnum, name='team_enum'), nullable=False)
    role_id = Column(String(40), ForeignKey('roles.id', ondelete="SET NULL"), nullable=True)

    role = relationship("Role", back_populates="users")  # ✅ optional: access Role from User

class Role(BaseModel):
    __tablename__ = 'roles'
    
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)

    users = relationship("User", back_populates="role")
    role_permissions = relationship('RolePermission', backref='role')


class Permission(BaseModel):
    __tablename__ = 'permissions'

    name = Column(Text, nullable=False)
    method = Column(Text, nullable=False)
    path = Column(Text, nullable=False)

    role_permissions = relationship('RolePermission', backref='permission')


class RolePermission(BaseModel):
    __tablename__ = 'role_permissions'

    role_id = Column(String(40), ForeignKey('roles.id', ondelete="CASCADE"), nullable=False)
    permission_id = Column(String(40), ForeignKey('permissions.id', ondelete="CASCADE"), nullable=False)
