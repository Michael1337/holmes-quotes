from flask import Flask, jsonify, request, render_template
import json
import random

app = Flask(__name__)

with open('quotes.json', 'r') as f:
    quotes = json.load(f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quote', methods=['GET'])
def get_quote():
    if 'id' in request.args:
        id = request.args['id']
        try:
            id = int(id)
            if id == 0:
                return jsonify({'quote': 'CTF{WEB_EXPLOITATION_GET_PARAMS_WBgZguAws4}'})
            for quote in quotes:
                if quote['id'] == id:
                    return jsonify({'id': quote['id'], 'quote': quote['quote']})
            return jsonify({'error': 'Quote not found'})
        except ValueError:
            return jsonify({'error': 'Quote not found'})
    else:
        quote = random.choice(quotes)
        return jsonify({'id': quote['id'], 'quote': quote['quote']})


if __name__ == '__main__':
    app.run()
