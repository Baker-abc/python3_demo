import flask

APP = flask.Flask(__name__)


@APP.route('/')
def index():
    return flask.render_template('index.html')


@APP.route('/hello/<name>')
def hello(name):
    return flask.render_template('hello.html', name=name)


@APP.route('/extends_master')
def extends_master():
    return flask.render_template('extends_master.html')


if __name__ == '__main__':
    APP.debug = True
    APP.run()
