# app.py
import math

import simplejson as json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from config import BaseConfig

app = Flask(__name__, static_url_path='')
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

API_V1 = '/api/v1/'


@app.route(API_V1 + "states", methods=["GET"])
def get_states():
    try:
        states = State.query.all()
        states_dict = {}
        for state in states:
            states_dict[state.id] = {
                'uf': state.uf
            }
        return json.dumps(states_dict)
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "cities", methods=["GET"])
def get_cities():
    try:
        cities = City.query.all()
        cities_dict = {}
        for city in cities:
            cities_dict[city.id] = {
                'name': city.name
            }
        return json.dumps(cities_dict)
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "locations", methods=["GET"])
def get_locations():
    try:
        locations = Location.query.all()
        locations_dict = {}
        for location in locations:
            locations_dict[location.id] = {
                'name': location.name
            }
        return json.dumps(locations_dict)
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "listing-types", methods=["GET"])
def get_listing_types():
    try:
        listing_types = ListingType.query.all()
        listing_types_dict = {}
        for listing_type in listing_types:
            listing_types_dict[listing_type.id] = {
                'name': listing_type.name
            }
        return json.dumps(listing_types_dict)
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "purposes", methods=["GET"])
def get_purposes():
    try:
        purposes = Purpose.query.all()
        purposes_dict = {}
        for purpose in purposes:
            purposes_dict[purpose.id] = {
                'name': purpose.name
            }
        return json.dumps(purposes_dict)
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "realties", methods=["GET"])
@app.route(API_V1 + "realties/<int:page>/<bool:asc>", methods=["GET"])
def get_realties(page=0, limit=50, asc=False):
    try:
        if asc:
            realties = Realty.query.order_by(Realty.published_on.asc()).limit(limit).offset(page * limit)
        else:
            realties = Realty.query.order_by(Realty.published_on.desc()).limit(limit).offset(page * limit)

        count = math.ceil(Realty.query.count() / limit) - 1

        realties_dict = {}
        for realty in realties:
            realties_dict[realty.id] = {
                'id': realty.id,
                'r_id': realty.rId,
                'title': realty.title,
                'published_on': realty.published_on.strftime('%d-%m-%Y %H:%M:%S')
            }
        return json.dumps({'data': realties_dict, 'count': count})
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "realty/<realtyId>", methods=["GET"])
@app.route(API_V1 + "realty/<realtyId>/<int:page>/<bool:asc>", methods=["GET"])
def get_realty(realtyId, page=0, limit=50, asc=False):
    try:
        if asc:
            realties = Realty.query.filter_by(rId=realtyId).order_by(Realty.published_on.asc()).limit(limit).offset(
                page * limit)
        else:
            realties = Realty.query.filter_by(rId=realtyId).order_by(Realty.published_on.desc()).limit(limit).offset(
                page * limit)

        count = math.ceil(Realty.query.filter_by(rId=realtyId).order_by(Realty.published_on.desc()).count() / limit) - 1

        realties_dict = {}
        for realty in realties:
            realties_dict[realty.id] = {
                'id': realty.id,
                'r_id': realty.rId,
                'title': realty.title,
                'published_on': realty.published_on.strftime('%d-%m-%Y %H:%M:%S')
            }
        return json.dumps({'data': realties_dict, 'count': count})
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + "realty-info/<realtyId>", methods=["GET"])
def get_realty_info(realtyId):
    try:
        realty = Realty.query.get(realtyId)

        realty_dict = {
            'id': realty.id,
            'title': realty.title,
            'published_on': realty.published_on.strftime('%d-%m-%Y %H:%M:%S'),
            'purpose': {
                'name': realty.purpose.name
            },
            'listing_type': {
                'name': realty.listing_type.name
            },
            'location': {
                'name': realty.location.name,
                'city': {
                    'name': realty.location.city.name,
                    'state': {
                        'uf': realty.location.city.state.uf
                    }
                }
            }
        }

        return json.dumps(realty_dict)
    except IntegrityError:
        return json.dumps({})


@app.route(API_V1 + 'info')
def app_status():
    return json.dumps({'server_info': BaseConfig.SQLALCHEMY_DATABASE_URI})


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
