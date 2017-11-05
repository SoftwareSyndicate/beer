from flask import request, current_app, redirect, json

def get_board_page():
    data = {
        'board': "taco"
    }
    return json.jsonify(data), 200
