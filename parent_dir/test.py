# Pre-installed modules
import os

# External modules
from flask import Flask, render_template

app = Flask(__name__)


def handle_test():
    """
    :returns: rendered template
    Injects file and name to an index.html
    """
    return render_template('index.html', file=f'{os.path.basename(__file__)=}', name=f'{__name__=}')


def set_me_up(raw_app: Flask):
    raw_app.add_url_rule(
        '/test', 'handle_test', handle_test, methods=['GET']
    )


def main():
    set_me_up(app)
    app.run(host='0.0.0.0', port=3000)


if __name__ == '__main__':
    main()

