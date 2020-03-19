"""
Data science API application that analyzes and gives scores for 
nfl fantasy football player trades.
"""


from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import numpy as np

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def root():
        """
        Root page, you should not land here.
        """
        return render_template('home.html')

    @app.route("/api/trade/", methods=['GET'])
    def analyze_trade():
        player0_id = request.args['player0_id']
        player1_id = request.args['player1_id']
        player2_id = request.args.get('player2_id')
        player3_id = request.args.get('player3_id')
        player4_id = request.args.get('player4_id')
        player5_id = request.args.get('player5_id')
        player6_id = request.args.get('player6_id')
        player7_id = request.args.get('player7_id')
        player8_id = request.args.get('player8_id')
        player9_id = request.args.get('player9_id')
        week = request.args['week']

        response = []

        response.append({player0_id: int(np.random.random_integers(100))})
        response.append({player1_id: int(np.random.random_integers(100))})

        return jsonify(response)

    @app.errorhandler(404)
    def page_not_found(error):
        return 'This page does not exist', 404

    return app

if __name__ == '__main__':
    app.run(debug=True, port=5000)