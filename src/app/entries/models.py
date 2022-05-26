# -- Imports -- #
# Third Party
from sqlalchemy import CheckConstraint, Enum
from sqlalchemy.orm import relationship, backref

# First Party
from .. import db
from . import db_enums as enums

# -- Many-to-Many tables -- #
rel_Entry_Src = db.Table("rel_entries_sourcebooks", db.Model.metadata,
    db.Column("entry_id", db.ForeignKey("entries.id")),
    db.Column("src_id", db.ForeignKey("books.id"))
)

# -- Independent Tables -- #
class Trait(db.Model):
    __tablename__ = 'traits'

    id = db.Column(db.String(100), primary_key=True)
    desc = db.Column(db.Text)

class SourceBook(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.String(100), primary_key=True)
    desc = db.Column(db.Text)
    publisher = db.Column(db.String(200), index=True)

# -- Base-level Entry -- #
class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, nullable=False)
    desc = db.Column(db.Text)

    src_book = relationship('SourceBook', secondary=rel_Entry_Src)
    src_page = db.Column(db.Integer)

    submodel = db.Column(db.String(100))
    __mapper_args__ = {
        'polymorphic_identity': 'entries',
        'polymorphic_on': submodel
    }

class Hazard(Entry):
    """Hazards are common obstacles encountered in dungeons."""
    __tablename__ = 'hazards'
    __mapper_args__ = {'polymorphic_identity': __tablename__}
    id = db.Column(db.Integer, db.ForeignKey('entries.id'), primary_key=True)

    level = db.Column(db.Integer, index=True)
    is_complex = db.Column(db.Boolean, default=False)

class Item(Entry):
    """Items are objects that can be purchased in game"""
    __tablename__ = 'items'
    __mapper_args__ = {'polymorphic_identity': __tablename__}
    id = db.Column(db.Integer, db.ForeignKey('entries.id'), primary_key=True)

    price = db.Column(db.Integer, CheckConstraint('price>=0'))
    # bulk = db.Column(db.Integer)
    # bulk should be implemented as a custom type that allows L to be considered as 0.1
    level = db.Column(db.Integer)

class Action(Entry):
    """Actions or Activities are taken by players."""
    __tablename__ = 'actions'
    __mapper_args__ = {'polymorphic_identity': __tablename__}
    id = db.Column(db.Integer, db.ForeignKey('entries.id'), primary_key=True)

    trigger = db.Column(db.Text)
    requirements = db.Column(db.Text)
    action_type = db.Column(Enum(enums.ActionType))
    duration = db.Column(db.Integer, CheckConstraint('duration>0'))