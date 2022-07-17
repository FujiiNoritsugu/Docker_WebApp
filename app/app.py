from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logging
import traceback

if os.getenv('DEBUG') == '1':
    from test_model import Person
else:
    from mysql_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLITE_URI') if os.getenv('DEBUG') == '1' else os.getenv('MYSQL_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PORT'] = os.getenv('PORT')
app.logger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler(os.getenv('LOG_FILE'))
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)
log = app.logger


db = SQLAlchemy(app)


@app.route('/')
def index():
    log.debug('index')
    return 'Response Data'


@app.route('/another')
def another():
    log.debug('another')
    return 'Another Response'


@app.route('/test_request')
def test_request():
    log.debug('test_request')
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise_request/<exercise>')
def exercise_request(exercise):
    log.debug('exercise_request')
    return f'exercise_request:{exercise}'


@app.route('/show_html')
def show_html():
    log.debug('show_html')
    return render_template('./test_html.html')


@app.route('/try_rest', methods=['POST'])
def try_rest():
    try:
        # リクエストデータをJSONとして受け取る
        request_json = request.get_json()
        log.debug(f'request_json:{request_json} type:{type(request_json)}')
        name = request_json['name']
        log.debug(f'name:{name}')
        response_json = {"response_json": request_json}
    except Exception:
        log.error(traceback.format_exec())
    return jsonify(response_json)


@app.route('/person_search')
def person_search():
    log.debug('person_search')
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    try:
        search_size = request.args.get("search_size")
        log.debug(f'search_size:{search_size}')
        search_size = int(search_size)
        persons = db.session.query(Person).filter(Person.size > search_size)
    except Exception:
        log.error(traceback.format_exec())
    return render_template('./person_result.html', persons=persons, search_size=search_size)


@app.route('/try_html')
def try_html():
    log.debug('try_html')
    return render_template('./try_html.html')


@app.route('/show_data', methods=["GET", "POST"])
def show_data():
    log.debug('show_data')
    return request.form


@app.route('/try_css')
def try_css():
    log.debug('try_css')
    return render_template('./try_css.html')
