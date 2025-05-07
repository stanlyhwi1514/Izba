from extensions import db
from base.models import BaseModel


class Category(BaseModel,db.Model):
    __tablename__ = 'categories'

    name = db.Column(db.String(255), unique=True, nullable=False)
    display_order = db.Column(db.Integer)


class Prompt(BaseModel, db.Model):
    __tablename__ = 'prompts'

    category_id = db.Column(db.String(40), db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    display_order = db.Column(db.Integer)



class FocusCategory(BaseModel,db.Model):
    __tablename__ = 'focus_categories'
    name = db.Column(db.String(255), unique=True, nullable=False)
    display_order = db.Column(db.Integer)



#checking commit 
#checking commit 2