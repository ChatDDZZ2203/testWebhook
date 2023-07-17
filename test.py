from flask import Flask

app = Flask(__name__)

@app.route('/my_route', methods=['GET', 'POST'])
def simple():
    return f'Hello from my route, __name__: {__name__}'


if __name__ == '__main__':
    app.run('0.0.0.0', os.getenv('PORT', 3000))

