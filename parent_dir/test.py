# Pre-installed modules
import os

# External modules
from flask import Flask, render_template, Blueprint

app = Flask(__name__)
js_blueprint = Blueprint('js', __name__, static_folder='static')
app.register_blueprint(js_blueprint)


@app.route('/tft', methods=['GET'])
def handle_test():
    """
    :returns: rendered template
    Injects file and name to an index.html
    """
    return render_template('index.html', file=f'{os.path.basename(__file__)=}', name=f'{__name__=}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
