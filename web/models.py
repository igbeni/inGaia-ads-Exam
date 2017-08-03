# models.py
from app import db

class State(db.Model):
    __tablename__ = 'state'

    id = db.Column(db.String, primary_key=True)
    uf = db.Column(db.String, nullable=False)

    cities = db.relationship(
        'City',
        backref='state',
        lazy='dynamic'
    )

    def __init__(self, uf):
        self.uf = uf

    def __repr__(self):
        return '<State %r>' % self.uf


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    state_id = db.Column(db.String, db.ForeignKey('state.id'))

    locations = db.relationship(
        'Location',
        backref='city',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<City %r>' % self.name


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city_id = db.Column(db.String, db.ForeignKey('city.id'))

    realties = db.relationship(
        'Realty',
        backref='location',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Location %r>' % self.name


class ListingType(db.Model):
    __tablename__ = 'listing_type'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    realties = db.relationship(
        'Realty',
        backref='listing_type',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ListingType %r>' % self.name


class Purpose(db.Model):
    __tablename__ = 'purpose'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    realties = db.relationship(
        'Realty',
        backref='purpose',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Purpose %r>' % self.name


class Realty(db.Model):
    __tablename__ = 'realty'

    id = db.Column(db.String, primary_key=True)
    rId = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    published_on = db.Column(db.DateTime, nullable=False)

    location_id = db.Column(db.String, db.ForeignKey('location.id'))
    listingType_id = db.Column(db.String, db.ForeignKey('listing_type.id'))
    purpose_id = db.Column(db.String, db.ForeignKey('purpose.id'))

    def __init__(self, title, published_on):
        self.title = title
        self.published_on = published_on

    def __repr__(self):
        return '<Realty %r>' % self.title