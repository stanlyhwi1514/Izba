from sqlalchemy import Column, String, Text, Boolean, ForeignKey, DateTime, func, CheckConstraint,Enum
from sqlalchemy.orm import relationship
from extensions import db  # adjust if your db import is different
from base.models import BaseModel  # assuming your BaseModel is in models.base
import enum
class Tenant(BaseModel):
    __tablename__ = 'tenants'

    name = Column(Text, nullable=False, unique=True)
    domain = Column(Text, unique=True)

    customers = relationship('Customer', backref='tenant', cascade="all, delete-orphan")
    users = relationship('User', backref='tenant', cascade="all, delete-orphan")


class Customer(BaseModel):
    __tablename__ = 'customers'

    tenant_id = Column(String(40), ForeignKey('tenants.id', ondelete="CASCADE"))
    name = Column(Text, nullable=False)
    industry = Column(Text)

    alerts = relationship('Alert', backref='customer', cascade='all, delete-orphan')

class TeamEnum(enum.Enum):
    accounts_team = 'accounts team'
    customer_team = 'customer team'

class User(BaseModel):
    __tablename__ = 'users'

    tenant_id = Column(String(40), ForeignKey('tenants.id', ondelete="CASCADE"), nullable=False)
    email = Column(Text, nullable=False, unique=True)
    full_name = Column(Text)
    password_hash = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    team = Column(enum.Enum(TeamEnum, name='team_enum'), nullable=False)
    role_id = Column(String(40), ForeignKey('roles.id', ondelete="CASCADE"))  # ✅ FK to roles.id with CASCADE delete


class Role(BaseModel):
    __tablename__ = 'roles'

    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)
    role_permissions = relationship('RolePermission', backref='role', cascade="all, delete-orphan")


class Permission(BaseModel):
    __tablename__ = 'permissions'

    name = Column(Text, nullable=False)
    method = Column(Text, nullable=False)
    path = Column(Text, nullable=False)

    role_permissions = relationship('RolePermission', backref='permission', cascade="all, delete-orphan")


class RolePermission(BaseModel):
    __tablename__ = 'role_permissions'

    role_id = Column(String(40), ForeignKey('roles.id', ondelete="CASCADE"), nullable=False)
    permission_id = Column(String(40), ForeignKey('permissions.id', ondelete="CASCADE"), nullable=False)
