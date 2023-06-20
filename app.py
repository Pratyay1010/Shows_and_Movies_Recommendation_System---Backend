from flask import Flask, request, jsonify
from flask_cors import CORS
from main import recommend_show_netflix, recommend_show_amazon_prime, recommend_show_hotstar, recommend_show_hulu

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello World"



@app.route('/recommend-netflix', methods=['POST'])
def recommend_netflix():
    data = request.get_json()
    show_name = data['variable']

    poster, recommended_shows = recommend_show_netflix(show_name)

    return jsonify({'variable1':poster, 'variable2':recommended_shows})



@app.route('/recommend-amazon-prime', methods=['POST'])
def recommend_amazon_prime():
    data = request.get_json()
    show_name = data['variable']

    poster, recommended_shows = recommend_show_amazon_prime(show_name)

    return jsonify({'variable1':poster, 'variable2':recommended_shows})




@app.route('/recommend-hulu', methods=['POST'])
def recommend_hulu():
    data = request.get_json()
    show_name = data['variable']

    poster, recommended_shows = recommend_show_hulu(show_name)

    return jsonify({'variable1':poster, 'variable2':recommended_shows})




@app.route('/recommend-hotstar', methods=['POST'])
def recommend_hotstar():
    data = request.get_json()
    show_name = data['variable']

    poster, recommended_shows = recommend_show_hotstar(show_name)

    return jsonify({'variable1':poster, 'variable2':recommended_shows})

if __name__ == '__main__':
    app.run(debug=True)