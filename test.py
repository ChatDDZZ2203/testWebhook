import os

from flask import Flask, render_template, Blueprint

app = Flask(__name__)
js_blueprint = Blueprint('js', __name__, static_folder='static')
app.register_blueprint(js_blueprint)


@app.route('/t', methods=['GET'])
def simple():
    return render_template('index.html', file=os.path.basename(__file__), name=__name__)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)

