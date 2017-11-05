from flask import request, current_app, redirect, json
import urllib

def get_board_page():
    board = request.args.get('board')
    page = request.args.get('page')

    with urllib.request.urlopen('https://a.4cdn.org/' + board + "/" + page + ".json") as response:
        data = response.read()
        return data, 200


def get_thread():
    board = request.args.get('board')
    thread = request.args.get('thread')    

    with urllib.request.urlopen('https://a.4cdn.org/' + board + "/thread/" + thread + ".json") as response:
        data = response.read()
        return data, 200
    
