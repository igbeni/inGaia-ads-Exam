# app.py

import simplejson as json
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from config import BaseConfig

app = Flask(__name__, static_url_path='')
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

API_V1 = '/api/v1/'


@app.route(API_V1 + 'info', methods=["GET"])
def app_status():
    return json.dumps({'server_info': BaseConfig.SQLALCHEMY_DATABASE_URI})


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')


@app.route(API_V1 + "realties_asc", methods=["GET"])
@app.route(API_V1 + "realties_asc/<int:page>", methods=["GET"])
def get_realties_asc(page=0, limit=50):
    sql = text('SELECT id, "rId", title, published_on FROM realty ORDER BY published_on ASC LIMIT ' + str(
        limit) + ' OFFSET ' + str(page * limit))
    result = db.engine.execute(sql)
    realties = []
    for row in result:
        realties.append({'id': row[0], 'r_id': row[1], 'title': row[2], 'published_on': row[3]})

    return jsonify({'data': realties, 'count': Realty.query.count()})


@app.route(API_V1 + "realties_desc", methods=["GET"])
@app.route(API_V1 + "realties_desc/<int:page>", methods=["GET"])
def get_realties_desc(page=0, limit=50):
    sql = text('SELECT id, "rId", title, published_on FROM realty ORDER BY published_on DESC LIMIT ' + str(
        limit) + ' OFFSET ' + str(page * limit))
    result = db.engine.execute(sql)
    realties = []
    for row in result:
        realties.append({'id': row[0], 'r_id': row[1], 'title': row[2], 'published_on': row[3]})

    return jsonify({'data': realties, 'count': Realty.query.count()})


@app.route(API_V1 + "realty_log_asc/<realtyId>", methods=["GET"])
@app.route(API_V1 + "realty_log_asc/<realtyId>/<int:page>", methods=["GET"])
def get_realty_log_asc(realtyId, page=0, limit=50):
    sql = text(
        'SELECT id, "rId", title, published_on FROM realty WHERE "rId" = \'' + str(
            realtyId) + '\' ORDER BY published_on ASC LIMIT ' + str(
            limit) + ' OFFSET ' + str(page * limit))
    result = db.engine.execute(sql)
    realties = []
    for row in result:
        realties.append({'id': row[0], 'r_id': row[1], 'title': row[2], 'published_on': row[3]})

    return jsonify({'data': realties, 'count': Realty.query.count()})


@app.route(API_V1 + "realty_log_desc/<realtyId>", methods=["GET"])
@app.route(API_V1 + "realty_log_desc/<realtyId>/<int:page>", methods=["GET"])
def get_realty_log_desc(realtyId, page=0, limit=50):
    sql = text(
        'SELECT id, "rId", title, published_on FROM realty WHERE "rId" = \'' + str(
            realtyId) + '\' ORDER BY published_on DESC LIMIT ' + str(
            limit) + ' OFFSET ' + str(page * limit))
    result = db.engine.execute(sql)
    realties = []
    for row in result:
        realties.append({'id': row[0], 'r_id': row[1], 'title': row[2], 'published_on': row[3]})

    return jsonify({'data': realties, 'count': Realty.query.count()})


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


@app.route(API_V1 + 'search', methods=['POST'])
@app.route(API_V1 + 'search/<int:page>', methods=['POST'])
def search_text(page=0, limit=50):
    if request.method == 'POST':
        title = request.form['query']
        query = ''

        i = 0
        for s in title.split():
            if i > 0:
                query += ' & '
            query += s
            i += 1

        sql = text(
            'SELECT id, "rId", title, published_on FROM realty WHERE to_tsvector(title) @@ '
            'to_tsquery(\'' + query + '\') ORDER BY published_on DESC  LIMIT ' + str(
                limit) + ' OFFSET ' + str(page * limit))
        result = db.engine.execute(sql)
        realties = []
        for row in result:
            realties.append({'id': row[0], 'r_id': row[1], 'title': row[2], 'published_on': row[3]})

        sql = text(
            'SELECT count(*) FROM realty WHERE to_tsvector(title) @@ '
            'to_tsquery(\'' + query + '\')')
        result = db.engine.execute(sql)
        count = []
        for row in result:
            count.append(row[0])

        return jsonify({'data': realties, 'count': count[0]})


@app.route(API_V1 + "posts_by_cities", methods=["GET"])
def get_posts_by_cities():
    sql = text(
        'SELECT c.id, c.name, count(r.id) AS realty_number FROM realty r INNER JOIN location l ON'
        ' r.location_id = l.id INNER JOIN city c ON l.city_id = c.id GROUP BY c.id ORDER BY realty_number DESC')
    result = db.engine.execute(sql)
    cities = []
    for row in result:
        cities.append({'id': row[0], 'name': row[1], 'realty_number': row[2]})

    return jsonify({'data': cities})


@app.route(API_V1 + "realties_by_cities", methods=["GET"])
def get_realties_by_cities():
    sql = text(
        'SELECT c.id, c.name, count(DISTINCT("rId")) AS realty_number FROM realty r INNER JOIN location l ON'
        ' r.location_id = l.id INNER JOIN city c ON l.city_id = c.id GROUP BY c.id ORDER BY realty_number DESC')
    result = db.engine.execute(sql)
    cities = []
    for row in result:
        cities.append({'id': row[0], 'name': row[1], 'realty_number': row[2]})

    return jsonify({'data': cities})


if __name__ == '__main__':
    app.run(debug=True)
